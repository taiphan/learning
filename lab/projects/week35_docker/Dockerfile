FROM python:3.11-slim
WORKDIR /app
COPY ../week33_fastapi /app
COPY ../../lib /app/lib
COPY ../../data/sample_policy.txt /app/data/sample_policy.txt
RUN pip install --no-cache-dir fastapi uvicorn pydantic
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
