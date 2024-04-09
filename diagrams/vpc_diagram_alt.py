from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import ECS, ECR
from diagrams.aws.network import PrivateSubnet, Endpoint
from diagrams.aws.storage import S3
from diagrams.aws.management import Cloudwatch

with Diagram("", filename="vpc_diagram_alt", outformat="png"):

  with Cluster("AWS"):
    logs = Cloudwatch("Logs")
    ecr = ECR("ECR")
    s3 = S3("S3")
    
    
    with Cluster("VPC"):
      ecs = ECS("ECS Task")
      privateSubnet = PrivateSubnet("Private Subnet")

      ecs >> privateSubnet 

      privateSubnet >> Endpoint("VPC Gateway\nEndpoint") >> s3
      privateSubnet >> Endpoint("VPC Endpoint") >> ecr
      privateSubnet >> Endpoint("VPC Endpoint") >> logs
  