FROM python:3.6
ENV SLUGIFY_USES_TEXT_UNIDECODE yes
RUN pip install apache-airflow
RUN mkdir -p /opt/airflow
COPY sbin/airflow-entrypoint.sh /opt/airflow/entrypoint.sh
COPY dags/ /opt/airflow/dags
CMD ["sh", "/opt/airflow/entrypoint.sh"]