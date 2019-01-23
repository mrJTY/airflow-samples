FROM python:3.6
ENV SLUGIFY_USES_TEXT_UNIDECODE yes
ENV AIRFLOW_HOME /opt/airflow
RUN pip install apache-airflow
WORKDIR /opt/airflow
COPY dags /opt/airflow/dags
COPY airflow-entrypoint.sh /opt/airflow/airflow-entrypoint.sh
CMD ["sh", "airflow-entrypoint.sh"]