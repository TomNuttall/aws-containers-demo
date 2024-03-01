# Infastructure

## Overview

- CloudFormation: Used to deploy infastructure on AWS.
- GitHub action: deploy.yml runs on change to app folder. Builds app image and pushes to ECR

## Diagrams

### Install

Install graphvis

```bash
brew install graphviz
```

VirtualEnv

```bash
python3 -m venv env
source env/bin/activate
```

Install diagrams package

```bash
pip install diagrams
```

### Generate architecture diagram

```bash
python backend_diagram.py
```
