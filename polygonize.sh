#!/bin/bash

docker-compose -f docker-compose.yml build > /dev/null
docker-compose -f docker-compose.yml run --rm polygonizer gdal_polygonize.py -8 $@
