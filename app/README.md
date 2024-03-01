# App

## Run Locally

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

```
python src/app.py -envPath '../.env'
```

## Tests

- Uses [moto](http://docs.getmoto.org/en/latest/) for mocking aws services.
- Uses [requests-mocks](https://requests-mock.readthedocs.io) for mocking api requests.

### Usage

```
pytest
```
