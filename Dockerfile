FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask flask-cors flask-talisman

EXPOSE 8080

CMD ["python", "app.py"]
