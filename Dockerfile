FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app

WORKDIR /app
ENV FLASK_APP=web.py
EXPOSE 5000

CMD ["python", "app/web.py"]
