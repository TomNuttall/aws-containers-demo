# App

_Simple example app of reading file from event bucket, doing some processing and uploading output to report bucket_

- Uses [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html/) for aws services.

## Local S3

- Uses [Minio](https://hub.docker.com/r/bitnami/minio) for local S3 storage.

```
yarn s3:start
```

Setup bucket and add file [Minio Admin](http://localhost:9001/).

| Name                | Value       |
| ------------------- | ----------- |
| MINIO_ROOT_USER     | minio       |
| MINIO_ROOT_PASSWORD | miniosecret |

An access key and secret key will also be needed

## Enviroment

| Name             | Reason                   |
| ---------------- | ------------------------ |
| INGRESS_BUCKET   | Bucket for ingress zip   |
| REPORT_BUCKET    | Bucket for output        |
| S3_KEY           | Zip filename             |
| DEVELOPMENT      | Set to True to use minio |
| MINIO_ACCESS_KEY | minio                    |
| MINIO_SECRET_KEY | miniosecret              |

## Run Locally

```
yarn dev
yarn s3:stop
```

## Tests

- Uses [moto](http://docs.getmoto.org/en/latest/) for mocking aws services.

### Usage

```
yarn test
```
