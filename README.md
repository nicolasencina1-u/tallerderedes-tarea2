# Taller de Redes - Tarea 2: Análisis de Tráfico HTTP

Este proyecto consiste en la implementación de un entorno contenedorizado con Docker para analizar el tráfico del protocolo HTTP. Se configuró un servidor web Apache y un cliente en Python para generar peticiones, capturando y examinando los paquetes de red resultantes.

## Tabla de Contenidos
* [Información General](#información-general)
* [Tecnologías Utilizadas](#tecnologías-utilizadas)
* [Características](#características)
* [Configuración e Instalación](#configuración-e-instalación)
* [Uso](#uso)
* [Referencias utilizadas](#referencias-utilizadas)

## Información General
- El propósito de este proyecto es estudiar el comportamiento del protocolo HTTP a nivel de red.
- Implementamos una arquitectura cliente-servidor aislada mediante contenedores para analizar de forma limpia el intercambio de tráfico.
- Evaluamos las respuestas del servidor tanto para peticiones exitosas (código 200 OK) como para errores de ruta (código 404 Not Found).

## Tecnologías Utilizadas
- **Ubuntu** - versión `latest` (Imagen de DockerHub, base para los contenedores)
- **Apache httpd** - versión `2.5.1-dev` (Servidor Web compilado desde el repositorio oficial)
- **Python** - versión 3 (Para los scripts del cliente)
- **urllib3** - versión 2.7.0 (Librería cliente HTTP de Python)
- **tcpdump** - versión integrada en Ubuntu (Para la captura de tráfico en la interfaz de red)
- **Docker** - (Para la orquestación y despliegue del entorno)

## Características
- Servidor HTTP Apache funcional compilado desde el código fuente.
- Cliente HTTP automatizado capaz de realizar peticiones GET personalizadas.
- Captura automatizada de paquetes en formato `.pcap` dentro del entorno del cliente.
- Manejo de respuestas estándar exitosas y de rutas erróneas.

## Configuración e Instalación
Todos los requisitos y pasos detallados para construir las imágenes y levantar los contenedores de Docker (tanto cliente como servidor) se encuentran documentados en el archivo [SETUP.md](./SETUP.md).

## Uso
Para saber cómo iniciar la captura con `tcpdump`, realizar las consultas de prueba y extraer las capturas de red `.pcap` generadas, revisa el documento [USAGE.md](./USAGE.md).

## Referencias utilizadas
- Repositorio oficial de [apache/httpd](https://github.com/apache/httpd) para el código del servidor.
- Documentación oficial de [urllib3](https://urllib3.readthedocs.io/en/stable/user-guide.html) para el desarrollo de los scripts cliente.
  
## Video explicativo del levantamiento del servicio, comandos utilizados para el cliente y servidor
- https://drive.google.com/drive/folders/1ApnwHEtBamS0S7ECKC0IPEA4_AUajwqi
Nota: El video requiere iniciar sesión con el correo institucional para poder acceder.
