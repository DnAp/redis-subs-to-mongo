import os
import redis
import pymongo
import json
from json import JSONDecodeError

redisClient = redis.Redis(os.environ['REDIS_HOST'], os.environ['REDIS_PORT'])

mongoClient = pymongo.MongoClient(os.environ['MONGODB_DSN'])
mongodb = mongoClient[os.environ['MONGODB_DATABASE']]

collectionPrefix = os.environ['MONGODB_COLLECTION_PREFIX']

pubSub = redisClient.pubsub()
pubSub.psubscribe(os.environ['REDIS_CHANNEL'])
for item in pubSub.listen():
    # {'type': 'message', 'pattern': None, 'channel': b'channel', 'data': b'blah opd'}
    # print(item)
    if item['type'] != 'pmessage':
        continue
    try:
        data = json.loads(item['data'])
    except JSONDecodeError:
        data = {'data': item['data']}
    mongodb[collectionPrefix + item['channel'].decode("utf-8")].insert_one(data)
    # print('Inserted %s: %s' % (collectionPrefix + item['channel'].decode("utf-8"), data))
