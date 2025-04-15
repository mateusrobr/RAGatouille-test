from langchain_ollama.llms import OllamaLLM

def invoke_llm(model_name, context, question):
    llm = OllamaLLM(model=model_name)
    response = llm.invoke(f"""
    Você é um chatbot especializado em responder sobre editais de Processo Seletivo. 
    Utilizando como base o seguinte contexto: {context}, Responda a seguinte Pergunta: {question} .
    Seja conciso""")
    return response