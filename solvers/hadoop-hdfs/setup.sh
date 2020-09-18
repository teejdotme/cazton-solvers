#!/bin/bash

export PUID=$(id -u)
export PGID=$(id -g)
docker-compose -f ./docker/docker-compose.yml pull
docker-compose -f ./docker/docker-compose.yml build
docker-compose -f ./docker/docker-compose.yml up -d