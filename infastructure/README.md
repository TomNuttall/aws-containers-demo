# Infastructure

## Overview

- CloudFormation: Used to deploy infastructure on AWS.
- GitHub action: deploy.yml runs on change to app folder. Builds app image and pushes to ECR

## Architecture Diagram

<img
  src='../diagrams/backend_diagram.png'
  raw=true
  alt='AWS Backend Architecture Diagram'
  width="100%"
  height="auto"
/>

## VPC Notes

Consideration given to using a private subnet with S3 gateway endpoints and ECR interface endpoints. There is however an additional cost to having the interface endpoints provisioned even when not in use.

Therefore for this demo running with cheaper costs the VPC uses an Internet gateway for access to other aws services (ECR, S3, CloudFront).

<img
  src='../diagrams/vpc_diagram.png'
  raw=true
  alt='AWS VPC Diagram'
  width="100%"
  height="auto"
/>


