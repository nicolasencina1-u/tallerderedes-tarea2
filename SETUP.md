# SETUP

## Servidor

1. Entrar a la ruta `server/`

2. Construir imagen del servidor con tag (`-t`) `servidor_http`: `docker build -t servidor_http .`

3. Crear (y ejecutar) contenedor del servidor con nombre (`--name`) `servidor_http` a partir de la imagen ya creada: `docker run -d --name tallerderedes_server servidor_http`

## Cliente

1. Entrar a la ruta `client/`

2. Construir imagen de cliente con tag (`-t`) `cliente_http`: `docker build -t cliente_http .`

3. Crear (y ejecutar) contenedor del cliente con nombre (`--name`): `docker run -d -it --name tallerderedes_cliente cliente_http`