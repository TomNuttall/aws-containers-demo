from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import ECS, ECR
from diagrams.aws.network import InternetGateway, PrivateSubnet, PublicSubnet
from diagrams.aws.storage import S3
from diagrams.aws.management import Cloudwatch
from diagrams.onprem.network import Internet

with Diagram("", filename="vpc_diagram", outformat="png"):

  internet = Internet("Internet")

  with Cluster("AWS"):
    logs = Cloudwatch("Logs")
    ecr = ECR("ECR")
    
    
    with Cluster("VPC"):
      igw = InternetGateway("Internet Gateway")
      publicSubnet = PublicSubnet("PublicSubnet")
      privateSubnet = PrivateSubnet("Private Subnet")

      ecs = ECS("ECS Task")
      ecs >> privateSubnet 
      privateSubnet >> S3("S3")
    
    ecs >> publicSubnet
    publicSubnet >> igw
           
  igw >> internet
  internet >> logs
  internet >> ecr