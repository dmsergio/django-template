# official base image
ARG PYTHON_VERSION=3.11-slim-bullseye

FROM python:${PYTHON_VERSION} as python


###############
# Build stage #
###############
FROM python as build-stage

# system dependencies
RUN apt-get update && apt-get -y dist-upgrade && apt-get install -y \
    # dependencies for building Python packages
    build-essential \
    # psycopg2 dependencies
    libpq-dev

# Copy Python dependencies
COPY requirements .

# Create Python dependency and sub-dependency wheels
RUN pip wheel --wheel-dir /usr/src/app/wheels -r development.txt


#############
# Run stage #
#############
FROM python as run-stage

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# System dependencies
RUN apt-get update && apt-get -y dist-upgrade && apt-get install -y \
    # Dependencies for building Python packages
    build-essential \
    # translations dependencies
    gettext \
    # psycopg2 dependencies
    libpq-dev \
    # Check db status
    netcat \
    # Monitor and halt system processes
    procps \
    # Debug Celery tasks
    telnet \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Copy python dependency wheels from build-stage
COPY --from=build-stage /usr/src/app/wheels  /wheels/

# Use wheels to install python dependencies
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
	&& rm -rf /wheels/

# Django entrypoint.sh
COPY ./compose/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

# Django start
COPY ./compose/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app

# Run entrypoint.sh
ENTRYPOINT [ "/entrypoint" ]
