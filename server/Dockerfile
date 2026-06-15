FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    git build-essential autoconf libtool libtool-bin \
    libpcre2-dev libexpat1-dev wget python3 libcrypt-dev

WORKDIR /usr/local/src
RUN git clone https://github.com/apache/httpd.git

WORKDIR /usr/local/src/httpd
RUN git clone https://github.com/apache/apr.git srclib/apr
RUN git clone https://github.com/apache/apr-util.git srclib/apr-util

RUN ./buildconf
RUN ./configure --with-included-apr
RUN make
RUN make install

RUN echo "Si funciona. Atte. server :)" > /usr/local/apache2/htdocs/index.html
RUN chmod 644 /usr/local/apache2/htdocs/index.html

CMD ["/usr/local/apache2/bin/httpd", "-D", "FOREGROUND"]