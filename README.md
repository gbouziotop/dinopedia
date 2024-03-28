# Dinopedia

Dinopedia is a web application for Dinosaur Aficionados, implemented in [Django 4](https://docs.djangoproject.com/en/4.2/releases/4.0/), [Python 3.10](https://www.python.org/downloads/release/python-3100/) and [Docker](https://docs.docker.com/).

## Installation Instructions

1. Clone the project: `git clone https://github.com/gbouziotop/dinopedia.git`
2. The project can be run by running the `docker-compose up -d` command.

## Post Installation
1. To create a superuser you can use the command `make create-superuser`.
2. Visit the admin panel and login in `http://localhost:8000/admin/`. From there, you can add new users and dinosaurs in the system as per the requested specs.
3. The API documentation was built using swagger and OpenApi v3 and can be found at `http://localhost:8000/api/v1/`.
4. The available endpoints are summed up as follows:
   1. `api/v1/dinosaurs/`
   2. `api/v1/dinosaurs/<id>/`
   3. `api/v1/user-favorite-dinosaurs/`
   4. `api/v1/user-favorite-dinosaurs/<id>/`
   5. `api/v1/token/`
   6. `api/v1/token/refresh/`
   7. `api/v1/register/`
5. The test suite provided is implemented via the unittest framework and can be run by the command `make test_py`
6. [Flake8](https://flake8.pycqa.org/en/latest/) linter has been used to verify code quality against each commit. It can be run via the command `make linter_py`

A detailed guide to the API calls can be found in [APIGuide.md](https://github.com/gbouziotop/blob/main/APIGuide.md). file
