import os
import streamlit as st
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import chromadb
import openai

# Load environment variables
load_dotenv()

# Streamlit configuration
st.set_page_config(page_title="Financial Bot", page_icon="💬")
st.title("📖 Rich Dad Poor Dad - Financial Chatbot")

# Define file paths
document_dir = "./"
filename = "Rich Dad Poor Dad.pdf"
file_path = os.path.join(document_dir, filename)

# Load and process the data
@st.cache_data
def load_data(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()
    text_splitter = CharacterTextSplitter(chunk_size=10000, chunk_overlap=0)
    chunks = text_splitter.split_documents(pages)
    return chunks

# Load the data and display a success message
chunks = load_data(file_path)

# Set up embeddings and Chroma client
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
persist_directory = "./chroma_db"

# Create a new Chroma client and database
client = chromadb.PersistentClient(path="./chroma_db")
db = Chroma.from_documents(chunks, embeddings, persist_directory="./chroma_db", client=client)

# Main interaction area
st.info("Hello! How can I help you today?")

# User input section: Now using the prompt from text area directly
user_input = st.text_area("Please enter your financial prompt:")

# Button to get advice
if st.button("Get Advice"):
    # Use the user input (prompt) to search relevant documents
    retrieved_docs = db.similarity_search(user_input, k=5)  # k is the number of documents to retrieve the context

    # Function to create the document prompt
    def _get_document_prompt(docs):
        prompt = "\n"
        for doc in docs:
            prompt += "\nContent:\n"
            prompt += doc.page_content + "\n\n"
        return prompt

    # Create the formatted context for the GPT prompt
    formatted_context = _get_document_prompt(retrieved_docs)

    # Now, use the input from the text area as the prompt for GPT-4
    prompt = f"""
    ## SYSTEM ROLE
    You are a highly knowledgeable and creative chatbot designed to assist with financial advice based on the principles outlined in **Rich Dad Poor Dad**.  
    Your responses must be rooted exclusively in the provided content, focusing on explaining, comparing, and contextualizing key concepts.

    ## USER QUESTION
    The user has asked:  
    **"{user_input}"**

    ## CONTEXT
    Here is the relevant content from the technical books:  
    '''
    {formatted_context}
    '''

    ## GUIDELINES
    1. **Accuracy**:  
    - Use only the information provided in the `CONTEXT` section to answer the question.  
    - If the context does not contain relevant information, clearly state: "The provided context does not contain this information."  
    - Begin by explaining the significance of the user's question.  
    - Follow up with a structured explanation, including:  
        - The perspective of **Rich Dad**.  
        - The perspective of **Poor Dad**.  
        - A comparison of both approaches.  
    - Conclude by highlighting why the **Rich Dad** approach is advantageous.  
    - **Include an analogy** to simplify complex financial concepts and make the explanation easier to understand.

    2. **Formatting**:  
    - Keep the response concise and short with maximum of 5 lines.
    - If the answer is too long, split it into shorter sentences and write the continuation on the next line.  
    - Highlight **Rich Dad** and **Poor Dad** in **bold** for clarity.  
    - Ensure the user's question appears in **bold** to differentiate it from the answer.
    
    3. **Analogy**:  
   - Use a **relevant analogy** related with chocolate to simplify complex financial concepts and deepen the user's understanding.
   - Make sure the analogy is relatable and easily understandable, helping to connect abstract concepts with everyday experiences.

    4. **Transparency**:  
    - Reference the book title whenever possible to provide credibility to the response.  
    - Avoid adding opinions or speculation outside the given context.

    5. **Clarity**:  
    - Use concise and short, professional, and user-friendly language.  
    - Format the response in Markdown for enhanced readability.
    """

    # Set up GPT client and parameters
    client = openai.OpenAI()
    model_params = {
        'model': 'gpt-4o',
        'temperature': 0.7,  # Increase creativity
        'max_tokens': 4000,  # Allow for longer responses
        'top_p': 0.9,        # Use nucleus sampling
        'frequency_penalty': 0.5,  # Reduce repetition
        'presence_penalty': 0.6    # Encourage new topics
    }

    # Send the prompt to the GPT model
    messages = [{'role': 'user', 'content': prompt}]
    completion = client.chat.completions.create(messages=messages, **model_params, timeout=120)

    # Display the response from GPT
    answer = completion.choices[0].message.content
    st.write(answer)

