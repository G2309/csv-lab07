FROM python:3.12-alpine3.20

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY .env .env

CMD ["python", "-m", "streamlit","run", "main.py"]
