FROM resin/armv7hf-debian:jessie
MAINTAINER @BenKhz

RUN apt-get update && apt-get install python python-pip

RUN pip install pygame

COPY application.py /

CMD python /application.py
