FROM python:3.9.7

RUN mkdir /www
WORKDIR /www
RUN mkdir /requirements
COPY ./requirements/ ./requirements
RUN pip install --upgrade pip
RUN pip install -r ./requirements/local.txt
# separted in other dockerfile
# RUN pip install -r ./requirements/test.txt

COPY ./docker/entrypoint.sh /entrypoint.sh
# RUN chmod +x /entrypoint.sh

ENV PYTHONUNBUFFERED 1
ENV FLASK_APP src.flask_app.py
ENV FLASK_DEBUG 1
ENV FLASK_RUN_PORT 8000
EXPOSE 8000