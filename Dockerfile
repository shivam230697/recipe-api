FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
COPY ./requirement.txt /requirement.txt
RUN pip3 install -r /requirement.txt
RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
