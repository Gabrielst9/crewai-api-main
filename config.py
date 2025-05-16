#configuração do módulo de definições LLM
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

#carrega variáveis de ambiente
load_dotenv()

#configuração do LLM
def get_llm():
    #cria instância do LLM com configurações padrão
    return OpenAI(
        temperature=0.7,
        max_tokens=2000,
        model_name="gpt-3.5-turbo-instruct"
    )