# aws-containers-demo

Demo Project to explore setting up a Container workflow with EventBridge and S3 Events, ECR, ECS, Fargate and Docker.

Event from S3 on uploading zip files launches ECS task to process a csv file and upload some results to an S3 bucket.

## Architecture Diagram

<img
  src='./diagrams/backend_diagram.png'
  raw=true
  alt='AWS Backend Architecture Diagram'
  width="100%"
  height="auto"
/>
