def create_prompt(symptoms: str) -> str:
    return f"""
Você é um assistente clínico especializado em saúde mental.
Analise os sintomas: {symptoms}.
Forneça uma lista de diagnósticos prováveis e o nível de urgência (baixa, média, alta).
Responda de forma concisa.
"""
