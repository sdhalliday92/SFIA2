#!/bin/bash

source /home/jenkins/.bashrc

pwd

docker stack deploy --compose-file docker-compose.yml sfia2
