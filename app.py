import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain_classic.agents import initialize_agent, AgentType
from langchain_classic.callbacks import StreamlitCallbackHandler
import os 
from dotenv import load_dotenv

load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['HUGGING_FACE'] = os.getenv('HUGGING_FACE')

# Arxiv & Wikipedia tool
api_wrapper_arxiv=ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=250)
arxiv=ArxivQueryRun(api_wrapper=api_wrapper_arxiv)

api_wrapper_wiki=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=250)
wiki=WikipediaQueryRun(api_wrapper=api_wrapper_wiki)

search = DuckDuckGoSearchRun(name='Search')

st.title('Langchain - Chat using Search Engine')

if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {'role':"assistant",'content':"Hi, I'm a chatbot who can search the web. How can I help you?" }
    ]
for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])
    
prompt=st.chat_input(placeholder='What is Machine learning?')
if prompt:
    st.session_state.messages.append({'role':'user','content':prompt})
    st.chat_message('user').write(prompt)
    
    llm= ChatGroq(model_name='llama-3.3-70b-versatile',streaming=True)
    tools=[search,arxiv,wiki]
    
    search_agent = initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
                                    handling_parsing_errors=True)
    
    with st.chat_message('assistant'):
        st_cb = StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages,callbacks=[st_cb])
        st.session_state.messages.append({'role':'assistant','content':response})
        st.write(response)

    