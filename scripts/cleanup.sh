#!/bin/bash

docker service update --image sdhalliday92/service_1:latest --force sfia2_service_1
docker service update --image sdhalliday92/service_2:latest --force sfia2_service_2
docker service update --image sdhalliday92/service_3:latest --force sfia2_service_3
docker service update --image sdhalliday92/service_4:latest --force sfia2_service_4

docker system prune -f