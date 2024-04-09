from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import ECS, ECR
from diagrams.aws.network import InternetGateway, PrivateSubnet, PublicSubnet, Endpoint
from diagrams.aws.storage import S3
from diagrams.aws.management import Cloudwatch
from diagrams.onprem.network import Internet

with Diagram("", filename="vpc_diagram", outformat="png"):

  internet = Internet("Internet")

  with Cluster("AWS"):
    logs = Cloudwatch("Logs")
    ecr = ECR("ECR")
    s3 = S3("S3")
    
    
    with Cluster("VPC"):
      igw = InternetGateway("Internet\nGateway")
      s3Endpoint = Endpoint("VPC Gateway\nEndpoint")
      publicSubnet = PublicSubnet("Public Subnet")
      privateSubnet = PrivateSubnet("Private Subnet")

      ecs = ECS("ECS Task")
      ecs >> privateSubnet 
      privateSubnet >> s3Endpoint >> s3
    
    ecs >> publicSubnet
    publicSubnet >> igw
           
  igw >> internet
  internet >> [ecr, logs]