#!/bin/bash

source ~/.bashrc

pwd

docker stack deploy --compose-file docker-compose.yml sfia2
