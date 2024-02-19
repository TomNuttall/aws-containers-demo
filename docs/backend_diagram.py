from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import ECR, ECS, Fargate
from diagrams.aws.security import IAM
from diagrams.aws.integration import Eventbridge
from diagrams.onprem.ci import GithubActions
from diagrams.onprem.container import Docker

with Diagram("", filename="backend_diagram", outformat="png"):
  github_action_ecr = GithubActions("Github Action")
  docker_image = Docker("Docker App")

  with Cluster("AWS"):
    iam_role_ecr = IAM("IAM")
    ecr = ECR("Elastic Container Registry")

    with Cluster(""):
        ecs = ECS("Elastic Container Service")
        ecs << ecr
        Eventbridge("EventBridge") >> Edge(label="Run schedule once a day") >> Fargate("Fargate") >> ecs


  github_action_ecr >> Edge(label="Get ECR role") >> iam_role_ecr
  github_action_ecr >> docker_image >> Edge(label="Build + push image") >> ecr
