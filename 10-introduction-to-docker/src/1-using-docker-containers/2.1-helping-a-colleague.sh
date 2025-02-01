#!/bin/bash

docker run -name colleague_project -d my_project

docker ps -f "name=colleague_project"

docker logs colleague_project

