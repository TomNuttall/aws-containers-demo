FROM python:3-slim-bullseye as base
WORKDIR /usr/src/app

# Prod
FROM base as prod
COPY ./requirements-prod.txt ./
RUN pip install --no-cache-dir -r requirements-prod.txt

COPY ./src .

CMD [ "python", "./app.py" ]

# Test
FROM base as test
COPY ./requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY ./src ./src

RUN pytest