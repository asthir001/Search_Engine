# 🦜 LangChain Chat with Search Engine
An AI-powered search assistant built with Streamlit, LangChain, and Groq. This chatbot doesn't just rely on its training data; it can browse the live web, search scientific papers on Arxiv, and look up facts on Wikipedia in real-time.

## 🚀 Features
- **Multi-Tool Intelligence**: Automatically chooses between DuckDuckGo (web search), Wikipedia (facts), and Arxiv (research papers) based on your question.

- **High Performance**: Powered by the llama-3.3-70b-versatile model via Groq for lightning-fast responses.

- **Interactive UI**: A clean, chat-based interface built with Streamlit.

- **Thought Visualization**: Uses StreamlitCallbackHandler so you can see the agent's "reasoning" process as it searches.

## 🛠️ Tech Stack
LLM: Llama 3.3 (via Groq)

### Framework: LangChain

### Frontend: Streamlit

### Tools: DuckDuckGo Search, Wikipedia API, Arxiv API

## 📋 Prerequisites
Before running the app, ensure you have:

Python 3.9 or higher.

A Groq API Key (Get it at console.groq.com).

## ⚙️ Installation & Setup

### Clone the repository:
```bash
git clone https://github.com/ashtir001/Search_Engine.git
cd Search_Engine
```

### Create a Virtual Environment:
```bash
python -m venv venv
```

### Activate it Windows:
```bash
venv\Scripts\activate
```

### Activate it Mac/Linux:
```bash
source venv/bin/activate
```

###  Install Dependencies:
```bash
pip install -r requirements.txt
```

Configure Environment Variables: Create a .env file in the root directory and add your Groq key:

Plaintext
GROQ_API_KEY=your_actual_api_key_here

## 🏃 How to Run
Launch the Streamlit application by running:
```bash
streamlit run your_filename.py
```
(Replace your_filename.py with the actual name of your script, e.g., app.py)

### 🤖 Usage
Simply type your query into the chat input:

"What is the latest research on Quantum Computing?" (Triggers Arxiv)

"Who is the current Prime Minister of Ireland?" (Triggers DuckDuckGo)

"Explain the history of the Roman Empire" (Triggers Wikipedia)
