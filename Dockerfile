FROM python:3.10-alpine

COPY app /app

WORKDIR /app

RUN apk add  gcc

RUN apk add  g++

RUN pip install -r requirements.txt

CMD ["python", "run.py"]