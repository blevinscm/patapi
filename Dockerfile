# escape=`

FROM python:latest
ENV PYTHONUNBUFFERED 1

ADD /app /app/
WORKDIR /app
ADD requirements.txt /app/


RUN pip install -r requirements.txt