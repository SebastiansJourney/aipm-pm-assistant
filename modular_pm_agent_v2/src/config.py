import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables from .env locally
load_dotenv()

# Load GROQ_API_KEY from Streamlit secrets if not already set in environment
if "GROQ_API_KEY" not in os.environ:
    try:
        os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
    except Exception:
        pass

# Setup the LLM
LLM_MODEL = "llama-3.3-70b-versatile"
TEMPERATURE = 0.3

llm = ChatGroq(model=LLM_MODEL, temperature=TEMPERATURE)
