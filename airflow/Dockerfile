FROM python:3.6
WORKDIR /opt/airflow
COPY Makefile /opt/airflow/Makefile
RUN make install
COPY dags /opt/airflow/dags
CMD ["make", "airflow"]