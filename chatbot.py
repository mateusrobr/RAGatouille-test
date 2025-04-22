from llm import invoke_llm
from ragclass import Rag
from utils.util import get_index_full_path
from db.index_db import IndexDB
import os

options_list = ["Fazer uma pergunta ao bot.",
                "Criar um index com docs",
                "Selecionar um index existente"]


class Chatbot:

    def __init__(self):
        self.rag = Rag()
        self.index_db = IndexDB()
        pass


    def user_loop(self):
        while True:
            self.message_to_user()
            choice = input("Qual é sua escolha? ")

            if choice == "1": #Fazer pergunta
                self.user_prompt()
            
            elif choice == "2": #criar novo index
                self.create_new_index()
            elif choice == "3":# selecinar um novo index
                self.select_index()
            else:
                print("xD")

    def user_prompt(self,):
        flag = self.rag.is_index_selected()
        if not flag:
            print("Primeiro selecione um index! ")
            return


        question = input("Qual é sua pergunta? ")
        results = self.rag.get_results(question)
        context = ' '.join([result['content'] for result in results])
        response = invoke_llm(model_name="qwen:4b",context=context, question=question)
        print(response)

    def create_new_index(self):
        index_name = input("Qual o nome do index? ")
        doc_path = input("Qual é o path do documento a ser indexado? ")
        desc = input("De uma breve descricao sobre oque é este index: ")
        list_path = [doc_path]

        result = self.index_db.is_index_stored(index_name=index_name)
        if not result:
            try:
                self.rag.index(index_name=index_name, docs_path=list_path)
                self.index_db.add_index(index_name=index_name, desc=desc)
            except Exception as e:
                    print(f"Erro: {e}")
    
    def select_index(self,):
        print("Selecione um index: ")
        results = self.index_db.get_all_indexes()
        for result in results:
            print(f"Nome do index: {result[1]}\nDescricao do index: {result[2]}")
            print("--------------------------------")
        choice_index = input("Qual index? (Digite o nome) ")
        index_full_path = get_index_full_path(choice_index)
        
        self.rag.select_existing_index(index_full_path)
        print("Index selecionado.")
        

    def message_to_user(self):
        print("-------------------Menu-------------------")
        print("Selecione a opção: \n")
        for i, option in enumerate(options_list):
            print(f"{i + 1}. {option}")


