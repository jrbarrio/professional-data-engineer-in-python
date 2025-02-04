FROM docker.io/library/ubuntu
RUN apt-get update
RUN apt-get install -y python3
COPY /app/requirements.txt /app/requirements.txt
COPY /app/pipeline.py /app/pipeline.py