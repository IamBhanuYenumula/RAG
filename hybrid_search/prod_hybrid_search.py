from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_experimental.text_splitter import SemanticChunking
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import os

embeddings = OllamaEmbeddings(model="bge-m3")
