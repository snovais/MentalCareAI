from transformers import pipeline, AutoTokenizer
import logging
from pydantic import BaseModel
from app.core.utils import create_prompt

logging.basicConfig(level=logging.INFO)

class SymptomInput(BaseModel):
    sintomas: str

# Modelo Flan-T5-small da Hugging Face
#MODEL_NAME = "google/flan-t5-small"
MODEL_NAME = "google/flan-t5-xl"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, 
                                          clean_up_tokenization_spaces=True,
                                            torch_dtype="auto",
                                          low_cpu_mem_usage=True
                                        )


# Pipeline correto para T5 (seq2seq)
generator = pipeline(
    "text2text-generation",
    model=MODEL_NAME,
    tokenizer=tokenizer,
    device_map="cpu"  # usa GPU se disponível
)

def get_diagnosis_from_llm(symptoms: str) -> str:
    try:
        prompt = create_prompt(symptoms)
        response = generator(
            prompt,
            max_new_tokens=150,
            temperature=0.6,
            do_sample=True,
            top_p=0.9
        )

        if MODEL_NAME.startswith("google/flan-t5"):
            # A resposta do Flan-T5 vem em um formato diferente
            return response[0]["generated_text"]
        else:
            output_text = response[0]["generated_text"]
            return output_text[len(prompt):].strip()

    except Exception as e:
        logging.error(f"Erro ao gerar diagnóstico: {e}")
        raise e  # Isso fará o FastAPI retornar 500 com detalhes no log

