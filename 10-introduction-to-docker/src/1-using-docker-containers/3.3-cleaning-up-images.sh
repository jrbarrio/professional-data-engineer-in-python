#!/bin/bash

docker rmi ubuntu

docker container prune

docker image prune -a