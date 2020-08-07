#!/bin/bash

source /home/jenkins/.bashrc

pwd

# env  \ 
# MYSQL_USER="${MYSQL_USER}" \
# MYSQL_PASSWORD="${MYSQL_PASSWORD}" \
# MYSQL_HOST="${MYSQL_HOST}" \
# MYSQL_PORT="${MYSQL_PORT}" \
# MYSQL_DB_NAME="${MYSQL_DB_NAME}" \
# SECRET_KEY="${SECRET_KEY}" \

# sed -i "s/\${MYSQL_USER}/${MYSQL_USER}/g;" docker-compose.yml
# sed -i "s/\${MYSQL_PASSWORD}/${MYSQL_PASSWORD}/g;" docker-compose.yml
# sed -i "s/\${MYSQL_HOST}/${MYSQL_HOST}/g;" docker-compose.yml
# sed -i "s/\${MYSQL_PORT}/${MYSQL_PORT}/g;" docker-compose.yml
# sed -i "s/\${MYSQL_DB_NAME}/${MYSQL_DB_NAME}/g;" docker-compose.yml
# sed -i "s/\${SECRET_KEY}/${SECRET_KEY}/g;" docker-compose.yml
docker stack deploy --compose-file docker-compose.yml sfia2
