FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
