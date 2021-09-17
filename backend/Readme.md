# Backend con python y FastAPI

## Cómo ejecutarlo

### Python y virtualenv (Opcion 1)

1. Descargar python desde [aqui](https://www.python.org/downloads/), version 3.*.
2. Instalar Python, asegurarse de escoger la opción de agregar al PATH en la instalación
3. Abrir una terminal/consola e ir a la carpeta del proyecto 
    - *```pip install virtualenv```
    - *```virtualenv env```
    - ```source env/bin/activate```
    - *```pip install -r requirements.txt``` 
    - ```python app.py```
    
 \*solo deben hacerse la primera vez

### Docker (Opcion 2)

1. Descargar docker desde [aquí](https://docs.docker.com/get-docker/)

2. Abrir una terminal/consola e ir a la carpeta del proyecto 
    - *```docker build --tag my-app```
    - *```docker run --rm -p 8080:8080 myapp```

## Cómo probarlo

Una vez que se esta ejecutando, sea la opción 1 o 2,
ir a un navegador y escribir _localhost:8080_ esto deberia motrar un mensaje de la siguiente forma ```{"mensaje":"Bienvenido a mi aplicación"}```