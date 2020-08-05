#!/bin/bash

echo $(docker images)

docker build --no-cache -t sdhalliday92/service_1 ./Service_1
docker push sdhalliday92/service_1:latest

docker build --no-cache -t sdhalliday92/service_2 ./Service_2
docker push sdhalliday92/service_2:latest

docker build --no-cache -t sdhalliday92/service_3 ./Service_3
docker push sdhalliday92/service_3:latest

docker build --no-cache -t sdhalliday92/service_4 ./Service_4
docker push sdhalliday92/service_4:latest

echo $(docker images)