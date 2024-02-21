# Bookstore API

Sample description

## Getting started

> *Make sure you have `pyenv` and `docker` installed*

Install python version as specified in `pyproject.toml` (3.11.1) and set as local:

```
pyenv virtualenv 3.11.1 bookstore_api && pyenv local bookstore_api
```

> *Optional: update pip with `python3.11 -m pip install --upgrade pip`*

Set your IDE to use this virtual environment and install requirements:

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

---

# Notes for running k8s cluster in `minikube`

>*Have `minikube` installed. For mac `brew install minikube`*

Start `minikube` with

```
minikube start
```

When everything is loaded create k8s infrastructure

```
kubectl apply -f k8s/deployment.yml -f k8s/service.yml -f k8s/secret.yml -f k8s/db_manifest.yml
```

Get URL to connect to the service with

```
minikube service bookstore-api --url
```

> *This might throw an error as the service might not be running. That could be caused by LoadBalancer - it's provided by cloud providers and `minikube` doesn't support it.*
> 
> *The pod for the service might still be in `Pending` state. You can check that with `kubectl get pods`*
> 
> *It is possible to bypass this issue with `minikube tunnel` command in separate terminal window.*

When you visit the URL provided by `minikube`, you'll see the welcome message for Bookstore API.

However when you try to find a book with `<url>/book/1` you'll get an `Internal server error`.

That is because the database is not yet configured.  To do that you need to enter the Postgres pod and create schema, table and seed data.
You can do that with:

```
kubectl exec -it <postgres-pod-id> -- bash
```

Inside the pod:

```
psql -u postgres -p password -d bookstore_api
```

In `psql`:

```sql
CREATE SCHEMA IF NOT EXISTS bookstore;

CREATE TABLE IF NOT EXISTS bookstore.book (
id serial primary key,
name text not null,
year int not null,
author text not null
);

INSERT INTO bookstore.book
(name, author, year)
VALUES
('Terry Pratchett, Otec prasátek', 'Bill Kaye, Stephen Player', 2007),
('TERRY PRATCHETT DISCWORLD NOVEL COLLECTION.', 'TERRY. PRATCHETT', 2012),
('Terry Pratchett''s Discworld Coloring Book', 'Terry Pratchett', 2017),
('Sourcery', 'Terry Pratchett', 2014),
('Dodger', 'Terry Pratchett', 2019),
('Seriously Funny', 'Terry Pratchett', 2016),
('Nation', 'Terry Pratchett', 2009),
('The Carpet People', 'Terry Pratchett', 2015),
('Truckers', 'Terry Pratchett', 2015),
('Sekáč', 'Terry Pratchett, Jan Kantůrek', 2011);
```

This way you can directly create, delete and update the data.