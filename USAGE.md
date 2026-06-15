# USAGE

0. Ambos contenedores deben estar ejecutándose, confirmarlo con el comando `docker ps`
1. En un PowerShell aparte, iniciar captura de tráfico (con `tcpdump`) en cliente: `docker exec -it tallerderedes_cliente tcpdump -w /app/captura.pcap`

2. Obtener dirección IP del servidor: `docker logs tallerderedes_server`
El mensaje mostrado es como:
```
AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.17.0.2. Set the 'ServerName' directive globally to suppress this message
```

3. Realizar petición `GET` desde el cliente al servidor con ip `172.17.0.2`: `docker exec tallerderedes_cliente python3 consulta.py 172.17.0.2`

4. Realizar petición `GET` a una ruta errónea desde el cliente al servidor con ip `172.17.0.2`: `docker exec tallerderedes_cliente python3 consulta_falla.py 172.17.0.2`

5. En el PowerShell detener captura: `CONTROL + C`

6. En el PowerShell guardar captura localmente (extraer desde el contenedor a la ruta de ejecución del PowerShell): `docker cp tallerderedes_cliente:/app/captura.pcap .`