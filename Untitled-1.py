import os
import streamlit as st
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import openai
import chromadb

import sqlite3
import sys

required_version = (3, 35, 0)
current_version = sqlite3.sqlite_version_info

if current_version < required_version:
    sys.exit(
        f"Error: SQLite version {current_version} is installed, but version >= {required_version} is required. "
        "Please update SQLite on your system."
    )

# Load environment variables
load_dotenv()

# Streamlit configuration
st.set_page_config(page_title="Financial Bot", page_icon="💬")
st.title("📖 Rich Dad Poor Dad - Financial Chatbot")
