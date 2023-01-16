FROM ubuntu:22.04
LABEL maintainer="Ambassador4ik"

RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3.11 python3.11-dev pip -y
RUN python3.11 -m pip install --upgrade pip

COPY requirements.txt .
RUN python3.11 -m pip install -r requirements.txt

ADD src .

CMD python3.11 main.py
