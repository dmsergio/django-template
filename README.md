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
