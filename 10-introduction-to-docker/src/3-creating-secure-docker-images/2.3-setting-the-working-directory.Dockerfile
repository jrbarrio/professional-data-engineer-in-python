FROM ubuntu:22.04
RUN useradd -m repl
USER repl
WORKDIR /home/repl
RUN mkdir projects/pipeline_final
COPY /home/repl/project projects/pipeline_final