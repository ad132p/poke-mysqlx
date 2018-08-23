import mysqlx
import requests
import sys
import json

# Estabelecendo conexão com o banco de dados:
session = mysqlx.get_session({
    "host": "localhost",
    "port": 33060,
    "user": "root",
    "password": "senha"
})

schema = session.get_schema("pokeapi")

schema.create_collection("items", reuse=True)
collection = schema.get_collection("items")

item_url = "http://pokeapi.co/api/v2/item/"

for i in range(1,803):
    r = requests.get(item_url + str(i))
    item_json = json.loads(r.text)
    try:
        collection.add(item_json).execute()
    except:
        print(i)

session.close()
