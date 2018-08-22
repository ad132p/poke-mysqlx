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

schema.create_collection("pokemons", reuse=True)
collection = schema.get_collection("pokemons")

poke_url = "http://pokeapi.co/api/v2/pokemon/"

for i in range(1,803):
    r = requests.get(poke_url + str(i))
    poke_json = json.loads(r.text)
    collection.add(poke_json).execute()

session.close()
