FROM python:3.7-slim

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ENV REDIS_HOST=localhost
ENV REDIS_PORT=6379
ENV REDIS_CHANNEL="*"
ENV MONGODB_DSN="mongodb://localhost:27017/"
ENV MONGODB_DATABASE="pubsub"
ENV MONGODB_COLLECTION_PREFIX="channel_"

COPY . /app

CMD ["python", "bin/run.py"]
