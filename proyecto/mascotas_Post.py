from locust import HttpUser, task, between
import json
from utils.carga_Json import cargar_mascotas

class UsuarioTiendaMascotas(HttpUser):
    wait_time = between(1, 3)
    host = "https://petstore.swagger.io/v2"

    def on_start(self):
        self.mascotas = cargar_mascotas("data/data.json")
        self.indice = 0

    @task
    def agregar_mascota(self):
        if not self.mascotas:
            print("No se cargaron mascotas")
            return

        mascota = self.mascotas[self.indice]
        cabecera = {"Content-Type": "application/json"}
        datos_envio = json.dumps(mascota)

        print(f"Enviando mascota: {mascota['name']} con ID {mascota['id']}")  #  imprime la mascota solo para debug (test)

        with self.client.post("/pet", data=datos_envio, headers=cabecera, catch_response=True) as respuesta:
            if respuesta.status_code == 200:
                try:
                    resp_json = respuesta.json()
                    if resp_json.get("id") == mascota.get("id"):
                        respuesta.success()
                    else:
                        respuesta.failure(f"El ID en la respuesta no coincide: {resp_json.get('id')}")
                except json.JSONDecodeError:
                    respuesta.failure("La respuesta no es un JSON válido")
            elif respuesta.status_code == 405:
                respuesta.failure("Error 405: Método no permitido")
            else:
                respuesta.failure(f"Código HTTP inesperado: {respuesta.status_code}")

        # Avanza al siguiente índice de forma cíclica
        self.indice = (self.indice + 1) % len(self.mascotas)
