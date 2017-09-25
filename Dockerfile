FROM resin/armv7hf-debian:jessie
MAINTAINER @BenKhz

COPY apt-install.sh /
COPY requirements.txt /

RUN /apt-install.sh

RUN pip install -r /requirements.txt

COPY . /app

# Makes local copy of audio source file. Comment out when using remote file source.

COPY 01ANightOfDizzySpells.ogg /

WORKDIR /app

CMD python application_slim.py
