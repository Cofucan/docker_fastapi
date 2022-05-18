FROM python:3.10.4

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update

WORKDIR /work

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN adduser --disabled-password --gecos '' cofucan

RUN chown -R cofucan:cofucan /work

USER cofucan
