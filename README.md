# mongo-csfle-beanie-fastapi

![Continuous Integration and Delivery](https://github.com/jonwhittlestone/mongo-csfle-beanie-fastapi/workflows/CI/badge.svg)

A simple FastAPI app "CustomerDB" demonstrating Client-Side Field Level Encryption.

A **super-admin** app user can view PII, but a **customer-service-agent** cannot.

## Prerequisites

- Poetry
- Python 3.9
- Environment variables:
  ```
    MONGO_URL=""
    MONGO_USERNAME=""
    MONGO_PASSWORD=""
    MONGO_DATABASE=""
  ```

## To run server

```
$ python src/main.py
# Visit http://127.0.0.1:8228 in browser
```

## To run tests

```
$ pytest tests
$ poetry run python -m pytest -k "mongo_connection"     # run a specfic test
```
