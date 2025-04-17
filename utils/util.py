options_list = ["Fazer uma pergunta ao bot.",
                "Adicionar docs ao index"] # TO DO: Faze a verificação se ja existe ou nao 
def message_to_user(options_list=options_list):
    print("-------------------Menu-------------------")
    print("Selecione a opção: \n")
    for i, option in enumerate(options_list):
        print(f"{i + 1}. {option}")
    