## Django template

- [x] Create a [Django](https://www.djangoproject.com/) project.
- [x] Build and run the project with [Docker compose](https://docs.docker.com/compose/).
- [ ] Set up logs inside Django project.
- [ ] Create a example app in order to interact with it via APIRest and [DRF](https://www.django-rest-framework.org/).
- [ ] Authentication with [JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/).
- [ ] Document the APIRest with [Swagger](https://swagger.io/).
- [ ] Add tests with [pytest](https://docs.pytest.org/en/7.2.x/).
- [ ] Integrate the [django-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) package to debug requests/responses.
- [ ] Implements [Celery](https://docs.celeryq.dev/en/stable/).
- [ ] Python tools to ensure both quality code and security code.
- [ ] Continuos Integration (CI).

### Create Django project

1. Install Python (recommended use the latest version available).

    ```shell
    pyenv install {PYTHON_VERSION}
    pyenv shell {PYTHON_VERSION}
    ```

2. Create a Python virtual environment and activate it.

    ```shell
    python -m venv .venv
    source .venv/bin/activate
    ```

3. Install Django.

    ```shell
    pip install --upgrade pip
    pip install Django
    ```

4. Create the Django project.

    ```shell
    django-admin startproject {DJANGO_PROJECT_NAME}
    ```

5. Migrate and run the server.

    ```shell
    python {DJANGO_PROJECT_NAME}/manage.py migrate
    python {DJANGO_PROJECT_NAME}/manage.py runserver
    ```

### Build and run the project inside Docker containers

1. Create an environment file.

    ```shell
    cp .env.dist .env
    ```

2. Build the image.

    ```shell
    docker compose build --pull
    ```

3. Run the both services, one for Django app and another for Postgres data base.

    ```shell
    docker compose up -d
    ```
