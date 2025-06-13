import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Load your knowledge base text
loader = TextLoader("knowledge.txt")
documents = loader.load()

# Embed and store the documents
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
vectorstore = Chroma.from_documents(documents, embeddings)

# Build the RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(openai_api_key=openai_api_key),
    retriever=vectorstore.as_retriever()
)

# Interactive Q&A loop
print("Ask me something about LangChain (type 'exit' to quit):")
while True:
    query = input("> ")
    if query.lower() in ("exit", "quit"):
        print("Goodbye!")
        break

    result = qa_chain.run(query)
    print(f"🤖 {result}")


