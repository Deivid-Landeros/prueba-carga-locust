import json

def cargar_mascotas(ruta_Archivo):
    try:
        with open(ruta_Archivo, 'r', encoding='utf-8') as aux:
            data = json.load(aux)
        return data
    except json.JSONDecodeError as e:  # el archivo no es un JSON válido
        print("Error, el archivo data no es un archivo JSON valido")
        raise e
    except FileNotFoundError as e:     # no existe el archivo JSON
        print("Error, No se encontro el Archivo")
        raise e