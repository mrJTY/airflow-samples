FROM continuumio/miniconda3:4.5.12
WORKDIR /opt/airflow
COPY Makefile /opt/airflow/Makefile
RUN apt-get update
RUN apt-get install -y make gcc
RUN make install
COPY dags /opt/airflow/dags
CMD ["make", "airflow"]