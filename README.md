# ecs-demo

Demo Project: ECS task runs to process zip files uploaded to an S3 bucket.

## Architecture Diagram

<img
  src='./docs/backend_diagram.png'
  raw=true
  alt='AWS Backend Architecture Diagram'
  width="100%"
  height="auto"
/>

## Enviromemnt

| Name           | Reason                 |
| -------------- | ---------------------- |
| INGRESS_BUCKET | Bucket for ingress zip |
| REPORT_BUCKET  | Bucket for output      |
