from transformers import pipeline, AutoTokenizer

from app.core.utils import create_prompt
from pydantic import BaseModel

class SymptomInput(BaseModel):
    sintomas: str

# Modelo Flan-T5-small da Hugging Face
MODEL_NAME = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, clean_up_tokenization_spaces=True)

# Pipeline correto para T5 (seq2seq)
generator = pipeline(
    "text2text-generation",
    model=MODEL_NAME,
    tokenizer=tokenizer,
    device_map="cpu"  # usa GPU se disponível
)

def get_diagnosis_from_llm(symptoms: str) -> str:
    """
    Gera diagnóstico baseado nos sintomas informados.
    """
    prompt = create_prompt(symptoms)
    
    response = generator(
        prompt,
        max_new_tokens=150,
        do_sample=True,
        temperature=0.6,
        top_p=0.9
    )

    output_text = response[0]["generated_text"]
    print(response)

    # Remove o prompt inicial caso seja repetido
    return output_text[len(prompt):].strip()
