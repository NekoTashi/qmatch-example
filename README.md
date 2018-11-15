# Ejemplo Flask App con Docker

## Instalación (Windows)
- Activar Hyper-V.
- Descargar Docker desde [https://www.docker.com/](https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe).
- Dar privilegios a `Docker.app` cuando el instalador pregunte.

## Docker

Construir la imagen de Docker:

```shell
$ docker build -t qmatch_example .
```

Correr Docker Container:

```shell
$ docker run -p 8000:8000 qmatch_example
```

Para dejar el Docker Container en background:

```shell
$ docker run -d -p 8000:8000 qmatch_example
```

Verificar que Docker esté corriendo:

```shell
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
50d2139192f7        qmatch_example      "gunicorn -b0.0.0.0:…"   4 seconds ago       Up 3 seconds        0.0.0.0:8000->8000/tcp   lucid_poitras
```

## Endpoints

Comercios:

```json
customers = [
    {"id": 1, "name": "Google"},
    {"id": 2, "name": "Duck Duck GO"},
    {"id": 3, "name": "Yandex"},
    {"id": 4, "name": "Bing"},
    {"id": 5, "name": "Yahoo"},
    {"id": 6, "name": "Baidu"},
    {"id": 7, "name": "AOL"},
]
```

Endpoints:

| URL | Method |
|---|---|
| `/` | GET |
| `/customers` | GET ó POST |
| `/customers/:id` | GET |
