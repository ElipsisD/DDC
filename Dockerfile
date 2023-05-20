FROM python:3.11-alpine

WORKDIR /development
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev
RUN apk add gdal gdal-dev geos geos-dev

RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal
RUN export C_INCLUDE_PATH=/usr/include/gdal

RUN apk add --no-cache tzdata
ENV TZ=Asia/Krasnoyarsk
ENV LANG ru_RU.UTF-8
ENV LC_ALL ru_RU.UTF-8
RUN cp /usr/share/zoneinfo/Asia/Krasnoyarsk /etc/localtime

COPY requirements.txt /temp/requirements.txt
RUN pip install --no-cache-dir -r /temp/requirements.txt

COPY development /development

RUN adduser --disabled-password development-user

USER development-user
