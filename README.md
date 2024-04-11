# Trellis Law Assessment

This repository contains a app to convert number to english plain text.

## Requirements

- Python 3.9+
- Poetry

## Installation

```bash
poetry shell
poetry install
``` 

## Setup
1. Duplicate the `.env.example` file and rename it to `.env` 

2. In the `.env` file configure the `API_KEY` entry. The key is used for authenticating our API.

## Run It

1. Start your app with:

```bash
make run
```

or

```bash
docker build -t numbers-app .
docker run -d -p 8000:8000 numbers-app
```

2. Go to [http://localhost:8000/docs](http://localhost:8000/docs).
3. Click `Authorize` and enter the API key.
4. Use it

## Run Linting

```bash
make lint
```

## Run Tests

```bash
make test
```