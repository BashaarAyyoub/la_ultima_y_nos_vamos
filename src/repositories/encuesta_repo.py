from bson import ObjectId
from src.config import db  # Tu conexión a MongoDB

class EncuestaRepository:
    def __init__(self):
        self.collection = db["encuestas"]

    def crear_encuesta(self, encuesta_dict):
        result = self.collection.insert_one(encuesta_dict)
        return str(result.inserted_id)

    def obtener_encuesta(self, encuesta_id):
        return self.collection.find_one({"_id": ObjectId(encuesta_id)})

    def cerrar_encuesta(self, encuesta_id):
        self.collection.update_one(
            {"_id": ObjectId(encuesta_id)},
            {"$set": {"estado": "cerrada"}}
        )

    def listar_encuestas(self):
        return list(self.collection.find())
from src.repositories.encuesta_repo import EncuestaRepository

repo = EncuestaRepository()
id = repo.crear_encuesta({
    "pregunta": "¿Pizza o hamburguesa?",
    "opciones": ["Pizza", "Hamburguesa"],
    "estado": "activa"
})
print("Encuesta creada con ID:", id)
