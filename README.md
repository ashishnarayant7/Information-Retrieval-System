
# 📘 Information-Retrieval-System

An interactive PDF-based question answering application built with **Streamlit**, **LangChain**, **FAISS**, and **Google Generative AI (Gemini)**.  
Upload one or more PDF files, and the system will let you ask natural language questions about their contents. It uses embeddings + vector search to retrieve relevant chunks and a conversational chain to generate answers.

---

## ✨ Features
- 📄 **PDF ingestion**: Extracts text from uploaded PDF files.
- ✂️ **Text chunking**: Splits large documents into manageable chunks for embedding.
- 🔎 **Vector search**: Stores chunks in a FAISS vector database for fast retrieval.
- 🤖 **Conversational AI**: Uses Google Gemini (`gemini-pro`) to answer questions with context.
- 💬 **Memory**: Maintains chat history for multi-turn conversations.
- 🌐 **Streamlit UI**: Simple web interface for uploading files and asking questions.

---

## Tech Stack 🧰

* [**Python**](https://www.python.org/): The core programming language used for the backend logic and data processing.
* [**Streamlit**](https://streamlit.io/): Builds the interactive web interface and handles the chat UI.
* [**LangChain**](https://www.langchain.com/): Orchestrates the application flow, connecting the document data to the LLM.
* [**Google Generative AI (Gemini)**](https://ai.google.dev/): Provides the `gemini-pro` model for reasoning and `embedding-001` for vectorizing text.
* [**FAISS**](https://github.com/facebookresearch/faiss): A vector store that enables efficient similarity search to find relevant document chunks.
* [**PyPDF2**](https://pypi.org/project/PyPDF2/): A library used to parse and extract raw text from uploaded PDF files.
* [**python-dotenv**](https://pypi.org/project/python-dotenv/): Manages environment variables to keep sensitive API keys secure.

---

## ⚙️ Installation

Clone the repo and set up a virtual environment:

```bash
git clone https://github.com/your-username/Information-Retrieval-System.git
cd Information-Retrieval-System

# Create and activate venv
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
.\.venv\Scripts\activate    # Windows

# Install dependencies
pip install -U streamlit langchain faiss-cpu google-generativeai langchain-google-genai PyPDF2 python-dotenv
```

---

## 🔑 Environment Setup

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_google_api_key_here
```

You can get your API key from [Google AI Studio](https://ai.google.dev/).

---

## 🚀 Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

1. Upload one or more PDF files in the sidebar.  
2. Click **Submit & Process** to build the vector store.  
3. Ask questions in the text box.  
4. View answers and chat history in the main panel.

---

## 📂 Project Structure

```
Information-Retrieval-System/
│
├── app.py                # Streamlit UI
├── src/
│   └── helper.py         # Core functions (PDF parsing, embeddings, chain setup)
├── .env                  # API key (not committed)
├── requirements.txt      # Dependencies (optional)
└── README.md             # Project documentation
```

---

## 🧩 Helper Functions
- `get_pdf_text(pdf_docs)` → Extracts text from PDFs  
- `get_text_chunks(text)` → Splits text into chunks  
- `get_vector_store(text_chunks)` → Builds FAISS vector store with embeddings  
- `get_conversational_chain(vector_store)` → Creates conversational retrieval chain with Gemini  

---

## 🚧 Troubleshooting
- **`ModuleNotFoundError: dotenv`** → Install `python-dotenv` in your environment.  
- **`No module named 'langchain.text_splitters'`** → Upgrade LangChain (`pip install -U langchain`) and use the correct import path.  
- **Google API errors** → Ensure your `.env` file has a valid `GOOGLE_API_KEY`.  

---

## 📜 License
MIT License – feel free to use, modify, and share.
```

---

This README is ready to paste into your repo.  

👉 Do you also want me to generate a **requirements.txt** file with pinned versions so you and your teammates can install everything in one go?
