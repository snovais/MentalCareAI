# 🧠 MentalCareAI
Assistente LLM para Apoio ao Diagnóstico em Saúde Mental em CAPS

## Execução

### Local
uvicorn app.main:app --reload

### Docker
docker build -t mentalcareai .
docker run -p 8000:8000 mentalcareai

### Kubernetes
kubectl apply -f k8s-deployment.yaml

### Testes
pytest app/tests/test_api.py

## Licença
MIT © 2025 Sérgio Novais
