import os
import sys
from crewai import Crew
from dotenv import load_dotenv
from typing import Dict

#configura o path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# imports dos módulos
from core.agents import create_gerador_plano, create_formatador_plano, create_sugeridor_recursos
from core.tasks import gerar_plano, formatar_plano, sugerir_conteudo
from services.docx_generator import gerar_plano_aula

load_dotenv()
os.makedirs("output", exist_ok=True)

def coletar_inputs() -> Dict[str, str]:
    print("\n" + "="*50)
    print(" GERADOR DE PLANO DE AULA - CREWAI ".center(50, "="))
    print("="*50 + "\n")
    
    inputs = {
        "escola": input("Nome da Escola: ").strip(),
        "professor": input("Nome do Professor: ").strip(),
        "tema": input("Tema da Aula: ").strip(),
        "serie": input("Série/Ano: ").strip(),
        "duracao": input("Duração (ex: 50 min): ").strip() or "50 min"
    }
    
    #validação
    campos_obrigatorios = ['escola', 'professor', 'tema', 'serie']
    for campo in campos_obrigatorios:
        if not inputs[campo]:
            print(f"\nErro: O campo '{campo}' é obrigatório!")
            sys.exit(1)
    
    return inputs

def executar_crew(inputs: Dict[str, str]) -> Dict[str, str]:
    print("\n⏳ Configurando agentes e tarefas...")
    
    try:
        #criação dos agentes
        gerador = create_gerador_plano()
        formatador = create_formatador_plano()
        sugeridor = create_sugeridor_recursos()

        #criação das tarefas
        t1 = gerar_plano(gerador, inputs)
        t2 = formatar_plano(formatador, inputs, [t1])
        t3 = sugerir_conteudo(sugeridor, inputs)

        #configuracao do Crew
        crew = Crew(
            agents=[gerador, formatador, sugeridor],
            tasks=[t1, t2, t3],
            verbose=True
        )
        
        print("Agentes configurados com sucesso!")
        print("\nExecutando o fluxo de geração...\n")
        
        result = crew.kickoff()
        
        #processa os resultados
        conteudo_plano = t1.output.raw_output if hasattr(t1.output, 'raw_output') else str(t1.output)
        recursos = t3.output.raw_output if hasattr(t3.output, 'raw_output') else str(t3.output)
        
        return {
            "conteudo_plano": conteudo_plano,
            "recursos": recursos
        }
        
    except Exception as e:
        print(f"\nErro durante a execução: {str(e)}")
        sys.exit(1)

def main():
    try:
        inputs = coletar_inputs()
        resultados = executar_crew(inputs)
        
        print("\n📄 Gerando documento Word...")
        output_path = gerar_plano_aula(
            inputs=inputs,
            conteudo_plano=resultados["conteudo_plano"],
            recursos=resultados["recursos"]
        )
        
        if output_path:
            print(f"\nDocumento gerado com sucesso em: {output_path}")
        else:
            print("\nFalha ao gerar o documento final.")
            
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
        sys.exit(0)

if __name__ == "__main__":
    main()