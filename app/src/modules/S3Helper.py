import boto3
import os

MINIO_ENDPOINT = 'http://s3:9000'


class S3Helper:

    def __init__(self, bucket_name: str, development: bool):
        """ ."""

        self.bucket_name = bucket_name
        if development:
            self.s3_client = boto3.client(service_name='s3',
                                          endpoint_url=MINIO_ENDPOINT,
                                          aws_access_key_id=os.environ.get(
                                              'MINIO_ACCESS_KEY'),
                                          aws_secret_access_key=os.environ.get('MINIO_SECRET_KEY'))
        else:
            self.s3_client = boto3.client(service_name='s3')

    def download(self, filename: str, folder: str):
        """ ."""

        download_path = os.path.join(folder, filename)
        self.s3_client.download_file(self.bucket_name, filename, download_path)
        return download_path

    def upload(self, filename: str, folder: str):
        """ ."""

        upload_path = os.path.join(folder, filename)
        self.s3_client.upload_file(upload_path, self.bucket_name, filename)
