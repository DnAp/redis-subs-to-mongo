# Redis subs to mongodb

## How to use this image
Add to you docker-compose.yml file new service
```
  redis_subs_to_mongo:
    image: dnap/redis-subs-to-mongo
    environment:
      - REDIS_HOST=redis
      - REDIS_HOST=localhost
      - REDIS_PORT=6379
      - REDIS_CHANNEL=*
      - MONGODB_DSN=mongodb://localhost:27017/
      - MONGODB_DATABASE=pubsub
      - MONGODB_COLLECTION_PREFIX=channel_
```
