from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import ECS, ECR
from diagrams.aws.network import InternetGateway, PublicSubnet, Endpoint
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

      with Cluster("Public Subnet"):
        publicSubnet = PublicSubnet("Public Subnet")

        igw = InternetGateway("Internet\nGateway")
        s3Endpoint = Endpoint("VPC Gateway\nEndpoint")
        ecs = ECS("ECS Task")

      ecs >>  igw
      ecs >> s3Endpoint >> Edge(label="") << s3
           
  igw >> Edge(label="") << internet
  internet >> [ecr, logs]