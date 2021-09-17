import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.model import Model

app = FastAPI(title="Mi aplicacion", version="1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def initial_app():
    return {"mensaje": "Bienvenido a mi aplicación"}


@app.get("/saludo")
def greetings(name):
    if name:
        return {"mensaje": f"Hola {name}! Que gusto verte aqui!!."}
    return {"mensaje": f"Dime tú nombre, asi puedo saludarte"}


@app.post("/login")
def login(datos: Model):
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
