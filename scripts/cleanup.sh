#!/bin/bash

docker service update --image sdhalliday92/service_1:latest sfia2_service_1
docker service update --image sdhalliday92/service_2:latest sfia2_service_2
docker service update --image sdhalliday92/service_3:latest sfia2_service_3
docker service update --image sdhalliday92/service_4:latest sfia2_service_4

docker system prune -f