#!/bin/bash

docker pull docker.mycompany.com/spam_alice:v3

docker run docker.mycompany.com/spam_alice:v3

docker load -i spam_bob.tar

docker run spam_bob:v3