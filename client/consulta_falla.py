import urllib3
import sys

ip = sys.argv[1]
url = f"http://{ip}/falla.html"
print(f"Conectando a {url}")

http = urllib3.PoolManager()
respuesta = http.request('GET', url)
print(f"Estado: {respuesta.status}")
print("Respuesta:")
print(respuesta.data.decode('utf-8'))