# official base image
FROM python:3.11-slim-bullseye as python

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# system dependencies
RUN apt-get update \
    && apt-get -y dist-upgrade \
    # dependencies for building Python packages
    && apt-get install -y build-essential \
    # psycopg2 dependencies
    && apt-get install -y libpq-dev \
    # translations dependencies
    && apt-get install -y gettext \
    # additional dependencies
    && apt-get install -y procps telnet netcat \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
COPY ./requirements-dev.txt /requirements-dev.txt
RUN pip install -r requirements-dev.txt

# django entrypoint.sh
COPY ./compose/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

# django start
COPY ./compose/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app

# run entrypoint.sh
ENTRYPOINT [ "/entrypoint" ]

