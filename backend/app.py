from fastapi import FastAPI
import uvicorn
from models.model import Model

app = FastAPI(title="Mi aplicacion", version="1.0")


@app.get("/")
def initial_app():
    return {"mensaje": "Bienvenido a mi aplicación"}

@app.get("/saludo")
def greetings(name):
    return {"mensaje": f"Hola {name}! Que gusto verte aqui!!."}

@app.post("/login")
def login(datos:Model):
    datos = datos.dict()
    if datos["user"] and datos["passwd"]:
        if datos["user"] == "admin" and datos["passwd"] == "admin123":
            return {"mensaje": "Ha ingresado exitosamente"}
        else:
            return {"mensaje": "Datos incorrectos, intente de nuevo."}
    else:
        return {"mensaje": "Debe escribir usuario y contraseña"}


if __name__ == "__main__":
     uvicorn.run(app, host="0.0.0.0", port=8080)