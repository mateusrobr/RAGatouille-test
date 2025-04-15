from ragatouille import RAGPretrainedModel
from ragatouille.data import CorpusProcessor, llama_index_sentence_splitter
from llm import invoke_llm
from ragclass import Rag

options_list = ["Fazer uma pergunta ao bot.",
                "Adicionar docs ao index"] # TO DO: Faze a verificação se ja existe ou nao 
def message_to_user(options_list=options_list):
    print("-------------------Menu-------------------")
    print("Selecione a opção: \n")
    for i, option in enumerate(options_list):
        print(f"{i + 1}. {option}")
    

def main(): #Transformar esse método main em uma classe chatbot
    rag = Rag()


    while True:
        message_to_user()
        choice = input("Qual é sua pergunta? ")

        if choice == 1:
            question = input("Qual é sua pergunta? ")
            rag.search(question)
            '''results = RAG.search(query=question, k=top_k)
            context = ' '.join([result['content'] for result in results])
            print(context)
            response = invoke_llm(model_name="qwen:4b",context=context, question=question)
            print(response)'''
        
        elif choice == 2:
            pass


if __name__ == '__main__':
    main()