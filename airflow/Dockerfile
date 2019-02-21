FROM continuumio/miniconda:4.5.12
WORKDIR /opt/airflow
COPY Makefile /opt/airflow/Makefile
RUN make install
COPY dags /opt/airflow/dags
COPY airflow-entrypoint.sh /opt/airflow/airflow-entrypoint.sh
CMD ["sh", "airflow-entrypoint.sh"]