# mongo-csfle-beanie-fastapi

A simple FastAPI demonstrating Client-Side Field Level Encryption

## Prerequisites

- Poetry

## To run server

```
$ python src/main.py
# Visit http://127.0.0.1:8228 in browser
```

## To run tests

```
$ pytest tests
```

## Todos

### Github action to run tests

### Todos as failing tests/stubs

### TODO. set up mongo connection in FastAPI settings with env vars

### Github action to use secret for integration test

### TODO. test for unencrypted mongo connection through FastAPI

### TODO. integrate CSFLE with motor

### TODO. `manage.py` : reset script for field level encrypted and unencrypted documents in a Mongo collection

### TODO. Add Beanie with simple FastAPI route to list all documents without encryption

### TODO. Dockerise with makefile
