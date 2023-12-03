FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /simple_solutions

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .