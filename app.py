import os
import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from dotenv import load_dotenv
import openai
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from chromadb.config import Settings
import chromadb
from langchain.embeddings.openai import OpenAIEmbeddings



# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize Streamlit app
st.set_page_config(page_title="Financial Bot", page_icon="💬")
st.title("📖 Rich Dad Poor Dad - Financial Chatbot")

# Load PDF and initialize embeddings
document_dir = "./"
filename = "Rich Dad Poor Dad.pdf"
file_path = os.path.join(document_dir, filename)

@st.cache_data
def load_data(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()
    text_splitter = CharacterTextSplitter(chunk_size=10000, chunk_overlap=0)
    chunks = text_splitter.split_documents(pages)
    return chunks

chunks = load_data(file_path)

# Set up embeddings and database
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
client = chromadb.PersistentClient(path="./chroma_db")
db = Chroma.from_documents(chunks, embeddings, persist_directory="./chroma_db", client=client)

# User input
st.sidebar.header("Ask Your Financial Question")
user_question = st.sidebar.text_area("Enter your question here:")

if st.sidebar.button("Get Advice"):
    if user_question.strip():
        with st.spinner("Fetching the best financial advice..."):
            # Retrieve documents
            retrieved_docs = db.similarity_search(user_question, k=5)
            context = "\n".join([doc.page_content for doc in retrieved_docs])

            # Prepare the prompt
            prompt = f"""
            ## SYSTEM ROLE
            You are a chatbot designed to provide financial advice based on **Rich Dad Poor Dad** principles.
            ## USER QUESTION
            "{user_question}"
            ## CONTEXT
            {context}
            ## TASK
            Provide advice based on the context.
            """

            # Query GPT
            openai.api_key = api_key
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{'role': 'system', 'content': prompt}],
                temperature=0.7,
                max_tokens=800,
                top_p=0.9,
                frequency_penalty=0.5,
                presence_penalty=0.6
            )
            bot_response = response['choices'][0]['message']['content']
            st.success("Here's the financial advice:")
            st.write(bot_response)
    else:
        st.warning("Please enter a question before submitting.")

st.sidebar.markdown("### About This Bot")
st.sidebar.info("Built using LangChain, OpenAI, and Streamlit.")
