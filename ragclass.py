from ragatouille import RAGPretrainedModel
from llm import invoke_llm
from llama_index.readers.file import PDFReader
from pathlib import Path
from llama_index.core import SimpleDirectoryReader
from db.index_db import IndexDB

class Rag:

    def __init__(self,model="colbert-ir/colbertv2.0"):
        self.dict_indexes = {}
        self.RAG = RAGPretrainedModel.from_pretrained(model)
        self.index_db = IndexDB()

    def index(self, index_name,docs_path):
        doc_text = self._load_documents(docs_path)

        index_path = self.RAG.index(collection=doc_text,
                       index_name=index_name,
                       max_document_length=200,
                       split_documents=True)
        
        self.dict_indexes[index_name] = index_path

    def _load_documents(self,doc_path):
        reader = SimpleDirectoryReader(input_files=doc_path)
        documents = reader.load_data()
        list_texts = [document.text for document in documents]
        return list_texts

