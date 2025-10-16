"""def create_prompt(symptoms: str) -> str:
    return f
Você é um assistente clínico especializado em saúde mental.
Analise os sintomas: {symptoms}.
Forneça uma lista de diagnósticos prováveis e o nível de urgência (baixa, média, alta).
Responda de forma concisa.
"""

def create_prompt(symptoms: str) -> str:
    prompt = (
        "Você é um assistente médico especializado em saúde mental e trabalha em um CAPS-AD. "
        "Sua tarefa é analisar o seguinte relato clínico e identificar o diagnóstico mental mais provável. "
        "As possíveis condições incluem: Depressão, Ansiedade, Transtorno Bipolar, Esquizofrenia, "
        "Dependência Química ou Nenhum transtorno identificado. "
        "Forneça uma resposta curta e direta no seguinte formato:\n\n"
        "Diagnóstico provável: <condição>\n"
        "Urgência: <baixa/média/alta>\n"
        "Justificativa: <breve motivo baseado nos sintomas>\n\n"
        f"Relato clínico: {symptoms}\n"
        "Responda em português claro."
    )
    return prompt