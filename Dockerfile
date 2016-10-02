FROM ubuntu:16.04

RUN sed -i 's/archive.ubuntu.com/kr.archive.ubuntu.com/g' /etc/apt/sources.list

RUN apt-get update && apt-get -y install \
    python3 python3-pip \
    binutils

RUN mkdir /unmangle
COPY bin/ /unmangle/bin/
COPY web/ /unmangle/web/

RUN pip3 install -r /unmangle/web/requirements.txt

EXPOSE 8000
ENTRYPOINT /unmangle/web/manage.py
