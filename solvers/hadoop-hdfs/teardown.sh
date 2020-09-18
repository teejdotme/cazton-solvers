#!/bin/bash

export PUID=$(id -u)
export PGID=$(id -g)
docker-compose -f ./docker/docker-compose.yml down -v --remove-orphans

./cleanup.sh
