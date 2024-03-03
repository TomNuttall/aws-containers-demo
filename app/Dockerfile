FROM python:3-slim-bullseye as base
WORKDIR /usr/src/app

# Prod
FROM base as prod
COPY ./src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

CMD [ "python", "./app.py" ]

# Test
FROM base as test
COPY ./tests/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src
COPY ./tests ./tests

RUN pytest