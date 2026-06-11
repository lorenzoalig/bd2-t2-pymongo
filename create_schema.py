from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))

print("Connected!")

db = client.get_database("testing_schemas")

db.drop_collection("categorias")
db.create_collection("categorias", validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "title": "Categoria",
        "required": ["cod_categoria", "nome"],
        "additionalProperties": False,
        "properties": {
            "_id": {
                "bsonType": "objectId"
            },
            "cod_categoria": {
                "bsonType": "double",
                "minimum": 1,
                "maximum": 999,
                "description": "Apenas codigos entre 1 e 999 caracteres"
            },
            "nome": {
                "bsonType": "string",
                "minLength": 5,
                "maxLength": 30,
                "description": "Apenas strings entre 5 e 30 caracteres"
            },
            "cod_categoria_pai": {
                "bsonType": "double",
                "minimum": 1,
                "maximum": 999,
                "description": "Apenas codigos entre 1 e 999 caracteres"
            }
        }
    }
})

print("DDL was a success!")

db["categorias"].insert_one({
    "cod_categoria": 1.0,
    "nome": "categoria1"
})

print("Categoria added successfully!")

categorias = db["categorias"].find({})

print("Printando categorias:")

for c in categorias:
    print(c)



