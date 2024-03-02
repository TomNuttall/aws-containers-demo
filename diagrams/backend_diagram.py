from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import ECR, ECS, Fargate
from diagrams.aws.integration import Eventbridge
from diagrams.aws.management import Cloudwatch
from diagrams.aws.storage import S3
from diagrams.onprem.ci import GithubActions
from diagrams.onprem.container import Docker

with Diagram("", filename="backend_diagram", outformat="png"):
  github_action_ecr = GithubActions("Github Action")
  docker_image = Docker("Docker App")

  with Cluster("AWS"):
    ecr = ECR("ECR")

    with Cluster(""):
        fargate = Fargate("Fargate")
        S3("S3 Zip Data") >> Edge(label="Object Created") >> Eventbridge("EventBridge Rule") >> Edge(label="Launch") >> fargate
        
        with Cluster(""):
          ecs = ECS("ECS Task")
        
          fargate >> ecs >> Cloudwatch("Logs")
          ecs << Edge(label="Pull Image") << ecr
          ecs >> Edge(label="Process Data") >> S3("S3 Report")

  github_action_ecr >> Edge(label="Build + push image")  >> docker_image >> ecr
