FROM ubuntu:22.04
RUN apt-get update
RUN apt-get install -y python3

RUN curl https://assets.datacamp.com/production/repositories/6082/datasets/31a5052c6a5424cbb8d939a7a6eff9311957e7d0/pipeline_final.zip -o /pipeline_final.zip\nRUN unzip /pipeline_final.zip\nRUN rm /pipeline_final.zip