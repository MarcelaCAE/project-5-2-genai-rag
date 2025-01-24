import os
import streamlit as st
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import openai

# Load environment variables
load_dotenv()

# Streamlit configuration
st.set_page_config(page_title="Financial Bot", page_icon="💬")
st.title("📖 Rich Dad Poor Dad - Financial Chatbot")
