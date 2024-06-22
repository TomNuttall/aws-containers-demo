from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import ECS, ECR
from diagrams.aws.network import InternetGateway, PublicSubnet, Endpoint
from diagrams.aws.storage import S3
from diagrams.aws.management import Cloudwatch
from diagrams.onprem.network import Internet

with Diagram("", filename="vpc_diagram", outformat="png", direction="TB"):

    internet = Internet("Internet")

    with Cluster("AWS"):
        logs = Cloudwatch("Logs")
        ecr = ECR("ECR")
        s3 = S3("S3")
        s3Endpoint = Endpoint("VPC Gateway\nEndpoint")

        with Cluster("VPC"):
            igw = InternetGateway("Internet\nGateway")

            with Cluster("Public Subnet"):
                publicSubnet = PublicSubnet("Public Subnet")
                ecs = ECS("ECS Task")

        ecs >> igw
        ecs >> s3Endpoint >> s3

    igw >> Edge(label="") << internet
    internet >> [ecr, logs]
