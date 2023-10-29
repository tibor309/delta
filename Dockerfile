FROM python:3.11.6-slim-bookworm

WORKDIR /app

RUN apt update -y && apt install -y gcc

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]