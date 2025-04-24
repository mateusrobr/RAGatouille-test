from ragatouille import RAGPretrainedModel
from llm import invoke_llm
from llama_index.readers.file import PDFReader
from llama_index.core import SimpleDirectoryReader


path = ".ragatouille/colbert/indexes/"

class Rag:

    def __init__(self,model="colbert-ir/colbertv2.0"):
        self.dict_indexes = {}
        self.RAG = RAGPretrainedModel.from_pretrained(model)
        #self.index_db = IndexDB()
        self.is_index_selected_var = False
        self.model = model

    def index(self, index_name,docs_path):
        doc_text = self._load_documents(docs_path)

        self.RAG.index(collection=doc_text,
                       index_name=index_name,
                       max_document_length=200,
                       split_documents=True)
        
    def get_results(self,query):
        results = self.RAG.search(query=query)
        return results


    def _load_documents(self,doc_path):
        reader = SimpleDirectoryReader(input_files=doc_path)
        documents = reader.load_data()
        list_texts = [document.text for document in documents]
        return list_texts

    def select_existing_index(self,path_to_index):
        try:
            self.RAG = RAGPretrainedModel.from_pretrained(self.model).from_index(path_to_index)
            self.is_index_selected_var = True
        except Exception as e:
            print(f"Erro ao selecionar index: {e}")

    def is_index_selected(self):
        if self.is_index_selected_var:
            return True
        
        return False