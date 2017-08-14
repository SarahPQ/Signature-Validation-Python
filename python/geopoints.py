#!/usr/bin/env python3

from mongolib import MongoClient, Transaction
from elasticlib import Elasticsearch
from elasticsearch.exceptions import RequestError


import os


mongo = MongoClient(database=os.environ.get('db'),
                    host=os.environ.get('host'),
                    username=os.environ.get('username'),
                    password=os.environ.get('password'))
elastic = Elasticsearch(hosts=os.environ.get('elastic_endpoint'),
                        port=80)

index_name = 'tx_geo'


mapping = {
  "mappings": {
    "transaction": {
      "properties": {
        "location": {
          "type": "geo_point"
        }
      }
    }
  }
}

# elastic.indices.delete(index=index_name)

try:
    elastic.indices.create(index=index_name, body=mapping)
except RequestError:
    print("Index already exists")

acc = mongo.get_database(os.environ.get('db'))
t_collection = acc.get_collection('transactions')
transactions = t_collection.find({'targetUser.location': {"$exists":"true"}})

for transaction in transactions:
    t = Transaction(transaction)
    elastic.index(index=index_name,
                  doc_type='transaction',
                  body={'location': t.target_user.location.coordinates,
                        'text': 'a transaction'})
