FROM docker:1.8

RUN apk --update add python python-dev py-pip alpine-sdk && rm -rf /var/cache/apk/*
RUN pip install --upgrade pip
RUN pip install sh
RUN pip install docker-py
RUN apk --update add openssh-client  && rm -rf /var/cache/apk/*

ENV PYTHONPATH $PYTHONPATH:/usr/local/lib/packerbot

ADD src /usr/local/lib/packerbot

RUN mkdir /sandbox

WORKDIR /sandbox
