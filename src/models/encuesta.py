import uuid
from datetime import datetime, timedelta

class Encuesta:
    def __init__(self, pregunta, opciones, tipo, duracion):
        self.pregunta = pregunta
        self.opciones = opciones
        self.tipo = tipo
        self.estado = "activa"
        self.duracion = duracion

    def to_dict(self):
        return {
            "pregunta": self.pregunta,
            "opciones": self.opciones,
            "tipo": self.tipo,
            "estado": self.estado,
            "duracion": self.duracion
        }
