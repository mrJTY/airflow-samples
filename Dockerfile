FROM python:3.7.1-alpine3.8
ENV SLUGIFY_USES_TEXT_UNIDECODE yes
RUN apk add build-base
RUN pip install apache-airflow

