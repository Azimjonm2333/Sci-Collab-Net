# E-commerce API

## Quick Start

**NOTE**: The project uses Python 3.11, so need it installed first. It is recommended to use [`pyenv`](https://github.com/pyenv/pyenv) for installation.

**NOTE**: Root of the django project is at the `src` folder

Here is a short instruction on how to quickly set up the project for development:

1. Install [`poetry`](https://python-poetry.org/)
2. Clone
```bash
$ git clone https://github.com/azizjon-aliev/ecommerce_api.git
```
3. Install requierements:

```bash
$ poetry install
$ poetry shell
```

4. Install pre-commit hooks: `$ pre-commit install`
5. Initiate the database: `$ make migrate`
6. Add and setup .env file: `$ cp .env.example .env` -> edit `.env`
7. Manually create a superuser: `$ make initadmin`
8. Run the server: `$ make runserver`

### Use with Docker

For local development:

`$ docker-compose -f docker/docker-compose.yml -f docker/docker-compose.local.yml --env-file ./.env up -d --build`

Read more [here](https://docs.docker.com/compose/extends/)

### Use Postgres with Docker

The project used Postgres as db engine. To use postgres with docker:

1. Add `POSTGRES_DB=ecommerce_api, POSTGRES_USER=postgres, POSTGRES_PASSWORD=postgres` to `.env`
2. From project root run `$ docker run --rm --volume pgdata:/var/lib/postgresql/data --name pg --env-file ./.env -d -p 5432:5432 postgres:14-alpine`


### URL for
1. [Admin](http://0.0.0.0:80/admin)
2. [API DOCS](http://0.0.0.0:80/docs)