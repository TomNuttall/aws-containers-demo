# Infastructure

## Overview

- CloudFormation template used to deploy infastructure on AWS.
- GitHub action runs on push to main branch.
  - deploy.yml runs on change to app folder
    - Builds app image and pushes to ECR
