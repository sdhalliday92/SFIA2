#!/bin/bash

docker pull sdhalliday92/service_1

docker pull sdhalliday92/service_2

docker pull sdhalliday92/service_3

docker pull sdhalliday92/service_4

docker rmi $(docker images -f "dangling=true" -q)

