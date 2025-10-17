🧠 MentalCareAI
Assistente LLM para Apoio ao Diagnóstico em Saúde Mental em CAPS

Execução

Local ->
uvicorn app.main:app --reload and streamlit run frontend/app_frontend.py

Docker ->
docker build -t mentalcareai .

docker run -p 8501:8501 -p 8000:8000 mentalcareai:latest

Kubernetes ->
kubectl apply -f k8s-deployment.yaml

Testes ->
pytest app/tests/test_api.py

Licença
MIT © 2025 Sérgio Novais
