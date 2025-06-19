# Prueba de carga con Locust 

Prueba de carga sobre el servicio REST de Petstore, https://petstore.swagger.io/v2  

Usé Python con Locust para simular peticiones POST y validar respuestas.


---

## Archivos que incluye

- **utils/carga_Json.py** -> carga datos desde un JSON  

- **mascotas_Post.py** -> prueba principal que hace los POST  

- **data/data.json** -> datos de prueba  

- **README.md** -> este archivo  

---

## Requisitos

- Python 3.8 o más nuevo  

- Locust instalado:

  ```
  pip install locust
  ```

- Archivo `data/data.json` con datos válidos (se incluye archivo para test)

---

## Cómo se ejecuta

1. Clonar repo:

   ```
   git clone <url>
   cd <carpeta>
   ```

2. Instalar Locust:

   ```
   pip install locust
   ```

3. ejecutar prueba:

   ```
   locust -f mascotas_Post.py
   ```

4. Abrir:  
   http://localhost:8089  

5. Configurar usuarios y tasa de ingreso  

---

## Flujo resumido

- Se cargan los datos desde `data/data.json`  

- Se envían POST por cada mascota  

- Se valida el código de respuesta y contenido  

- Si algo falla, se deja en el reporte de Locust  

---

## Notas

Se controlan errores como;

- JSON inválido  

- Archivo no encontrado  

- Respuestas HTTP erróneas  

---

## Autor

David Landeros  
