from crewai import Task

def gerar_plano(agent, inputs):
    #cria tarefa para gerar plano de aula em markdown
    return Task(
        description=f"Gere um plano de aula sobre '{inputs['tema']}' para a série '{inputs['serie']}'",
        agent=agent,
        expected_output="Plano de aula completo em formato markdown",
        output_file="output/plano_bruto.txt"  # Garanta que está gerando este arquivo
    )

def formatar_plano(agent, inputs, context):
    #formata o plano com cabeçalho da escola
    return Task(
        description=f"Formate o plano de aula com cabeçalho da escola '{inputs['escola']}'",
        agent=agent,
        expected_output="Plano de aula formatado em markdown",
        output_file="output/plano_formatado.txt",
        context=context
    )

def sugerir_conteudo(agent, inputs):
    #busca recursos educacionais relacionados ao tema
    return Task(
        description=f"Busque recursos sobre '{inputs['tema']}'",
        agent=agent,
        expected_output="Lista de recursos em markdown",
        output_file="output/recursos.txt"
    )