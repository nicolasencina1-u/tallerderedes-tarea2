FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip tcpdump
RUN pip3 install urllib3 --break-system-packages

WORKDIR /app
COPY consulta.py .
COPY consulta_falla.py .

CMD ["/bin/bash"]