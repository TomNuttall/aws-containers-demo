# Infastructure

## Overview

- CloudFormation: Used to deploy infastructure on AWS.
- GitHub action: deploy.yml runs on change to app folder. Builds app image and pushes to ECR

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
