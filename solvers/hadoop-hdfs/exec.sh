#!/bin/bash

docker-compose -f ./docker/docker-compose.yml exec workspace /bin/bash -c "cd /hadoop/workspace && ./scripts/jobs-exec.sh"