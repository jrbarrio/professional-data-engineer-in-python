#!/bin/bash

docker build -t hello_image .

docker run --env NAME="Jorge" hello_image