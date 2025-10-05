def create_prompt(symptoms: str) -> str:
    return f"""
Você é um assistente clínico especializado em saúde mental.
Analise os sintomas: {symptoms}.
Forneça diagnósticos prováveis e nível de urgência (baixa, média, alta).
Responda em JSON.
"""
