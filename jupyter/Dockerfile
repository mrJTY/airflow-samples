FROM jupyter/base-notebook:fa9ee3692919
RUN pip install sqlalchemy
RUN pip install pandas
RUN pip install psycopg2
COPY jupyter_notebook_config.json /home/jovyan/.jupyter/jupyter_notebook_config.json