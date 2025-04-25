# Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh


WORKDIR /app

RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev \
    build-essential
    
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "lojaonline.wsgi:application", "--bind", "0.0.0.0:8000"]
