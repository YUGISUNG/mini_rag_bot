# 🧠 Mini RAG Bot

A lightweight Retrieval-Augmented Generation (RAG) chatbot powered by [LangChain](https://www.langchain.com/), [ChromaDB](https://www.trychroma.com/), and [OpenAI](https://platform.openai.com/).

> Built as a mini project for testing local RAG pipelines using `.txt` files and OpenAI embeddings.

---

## 🚀 Features

- 🔍 Loads a local `.txt` knowledge file for reference
- 🧠 Converts knowledge into OpenAI embeddings
- 🗃️ Stores those embeddings in ChromaDB
- 💬 Enables local Q&A over your private knowledge
- 🧪 Fully local development environment using Python & virtualenv

---

## 📁 File Overview

| File               | Purpose                                      |
|--------------------|----------------------------------------------|
| `.env`             | Required for your OpenAI API key (not included)|
| `rag_bot.py`       | Main script that runs the bot                |
| `knowledge.txt`    | Knowledge source for answering queries       |
| `.gitignore`       | Prevents secret files like `.env` from pushing |
| `README.md`        | You’re reading it!                           |

---

## 🛠️ Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/YUGISUNG/mini_rag_bot.git
   cd mini_rag_bot

