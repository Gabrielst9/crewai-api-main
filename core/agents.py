from crewai import Agent
from core.tools import FetchConteudoEducacionalTool
from config import get_llm

def create_gerador_plano():
    #cria um agente para gerar planos de aula estruturados
    return Agent(
        role="Gerador de Plano de Aula",
        goal="Criar planos de aula estruturados e objetivos",
        backstory="Você é um educador experiente e especialista em elaboração de planos de aula claros e didáticos.",
        tools=[],
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )

def create_formatador_plano():
    #organiza o plano de aula com formatação profissional
    return Agent(
        role="Formatador de Documento Educacional",
        goal="Organizar e estruturar o plano de aula com cabeçalho e formatação adequada",
        backstory="Você é responsável por entregar documentos organizados, com cabeçalho escolar e estrutura profissional.",
        tools=[],
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )

def create_sugeridor_recursos():
    #sugere conteúdos de apoio para o plano de aula
    return Agent(
        role="Especialista em Recursos Didáticos",
        goal="Sugerir conteúdos de apoio para enriquecer o plano de aula",
        backstory="Você conhece as melhores fontes de conteúdo educacional online e sabe como encontrar recursos relevantes para qualquer tema.",
        tools=[FetchConteudoEducacionalTool()],
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )
