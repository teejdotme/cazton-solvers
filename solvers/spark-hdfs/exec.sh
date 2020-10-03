#!/bin/bash

docker-compose -f ./docker/docker-compose.yml exec spark-app /bin/bash -c "/spark/app/submit.sh"

docker-compose -f ./docker/docker-compose.yml exec workspace /bin/bash -c "/hadoop/workspace/scripts/hdfs-reduce.sh"