#!/bin/bash

source /home/jenkins/.bashrc

pwd

env  \ 
MYSQL_USER="${MYSQL_USER}" \
MYSQL_PASSWORD="${MYSQL_PASSWORD}" \
MYSQL_HOST="${MYSQL_HOST}" \
MYSQL_PORT="${MYSQL_PORT}" \
MYSQL_DB_NAME="${MYSQL_DB_NAME}" \
SECRET_KEY="${SECRET_KEY}" \
docker stack deploy --compose-file docker-compose.yml sfia2
