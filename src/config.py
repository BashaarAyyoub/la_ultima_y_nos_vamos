import json
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["la_ultima_y_nos_vamos"]


def cargar_config():
    with open("config.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)
