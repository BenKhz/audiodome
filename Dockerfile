FROM resin/armv7hf-debian:jessie
MAINTAINER @BenKhz

COPY apt-install.sh /
COPY requirements.txt /

RUN /apt-install.sh

RUN pip install -r /requirements.txt

COPY application.py /

# This commented link is a sharable google drive link to a folder with source audio.
# Comment out when switching to a remotely sourced audio file.
# https://drive.google.com/drive/folders/0B3141YlVSsRgd1BxX043dHd4UUU?usp=sharing

# Makes local copy of audio source file. Comment out when using remote file source.
COPY 01ANightOfDizzySpells.ogg /

CMD python /application.py
