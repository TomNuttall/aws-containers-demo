# App

_Simple example app of reading file from event bucket, doing some processing and uploading output to report bucket_

- Uses [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html/) for aws services.

## Enviroment

| Name           | Reason                 |
| -------------- | ---------------------- |
| INGRESS_BUCKET | Bucket for ingress zip |
| REPORT_BUCKET  | Bucket for output      |
| S3_KEY         | Zip filename           |

## Run Locally

```
yarn dev
yarn stop
```

## Tests

- Uses [moto](http://docs.getmoto.org/en/latest/) for mocking aws services.

### Usage

```
yarn test
```
