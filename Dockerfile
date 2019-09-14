FROM osgeo/gdal:alpine-normal-latest

MAINTAINER Kevin Albers (kalbers33@gmail.com)

WORKDIR /app

RUN ln -s $(which python3) /usr/bin/python

CMD ["python3"]


