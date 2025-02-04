FROM ubuntu:22.04
RUN useradd -m repl
USER repl
RUN mkdir /home/repl/projects/pipeline_final
COPY /home/repl/project /home/repl/projects/pipeline_final