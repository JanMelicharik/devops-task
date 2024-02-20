# Bookstore API

Sample description

## Getting started

> *Make sure you have `pyenv` and `docker` installed*

Install python version as specified in `pyproject.toml` (3.11.1) and set as local:

```
pyenv virtualenv 3.11.1 bookstore_api && pyenv local bookstore_api
```

> *Optional: update pip with `python3.11 -m pip install --upgrade pip`*

Set your IDE to use this virtual environment.
Install requirements:

```
pip install --upgrade -r requirements.txt
```

## Running locally

To spin up containers for bookstore-api and Postgres DB run

```
docker compose up -d
```

### Documentation (Swagger)

To see an auto-generated documentation for Bookstore API, visit `http://localhost:8000/docs`

### Updating requirements

When you start using new package, add it to requirements with
```
pip freeze > requirements.txt
```

and to rebuild the Bookstore API image, run
```
docker compose up --build bookstore
```

## Testing

To run a full suite of tests, run:
```
docker compose up -d
docker exec -it bookstore-api /bin/bash
```

And from inside the container
```
> pytest
```

> *In case you want to see more info and logs for failing tests, you can run `pytest -vv -s`

>*To specify a single test or file, you can use `pytest -k <test_module.py>:<test_name>`*

---
# Ideas for future improvements
1) Add more and better endpoints for reading, writing and updating data
2) Validate data quality - Check upon import.
3) Setup automatic code formatting using pre-commit (black, pylint, isort)
4) Dependency management tool (Poetry)
5) Implement additional logging and tracking of request lifetime
6) Implement suite of tests using pytest
7) Better object management with pydantic models