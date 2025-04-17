from ragclass import Rag
from utils.util import message_to_user 
from db.index_db import IndexDB
import os


class Chatbot:

    def __init__(self):
        self.rag = Rag()
        self.index_db = IndexDB()
        pass


    def user_loop(self):
        while True:
            message_to_user()
            choice = input("Qual é sua escolha? ")

            if choice == "1":
                print("Selecione um index: ")
                results = self.index_db.get_all_indexes()
                for result in results:
                    print(result)
                choice_index = input("Qual index? ")


                #question = input("Qual é sua pergunta? ")
                #self.rag.search(question)
                '''results = RAG.search(query=question, k=top_k)
                context = ' '.join([result['content'] for result in results])
                print(context)
                response = invoke_llm(model_name="qwen:4b",context=context, question=question)
                print(response)'''
            
            elif choice == "2":
                index_name = input("Qual o nome do index? ")
                doc_path = input("Qual é o path do documento a ser indexado? ")
                list_path = [doc_path]

                result = self.index_db.is_index_stored(index_name=index_name)
                if not result and os.path.exists(doc_path):
                    try:
                        self.index_db.add_index(index_name=index_name)
                        self.rag.index(index_name=index_name, docs_path=list_path)
                    except Exception as e:
                        print(f"Erro: {e}")
                    

            
            else:
                print("xD")


