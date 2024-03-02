import boto3
import os
import argparse
from dotenv import load_dotenv
from pathlib import Path
from zipfile import ZipFile


def get_object(bucket_name, object_name):
  """ ."""
	
  print(bucket_name, object_name)
  if not bucket_name or not object_name:
    return
  
  client = boto3.client('s3')
  with open('temp.zip', 'wb') as file:
    client.download_fileobj(bucket_name, object_name, file)

  with ZipFile('temp.zip', 'r') as archive:  
    archive.extractall()

  print(os.listdir())

  #client.upload_file(file_name, os.envrion("REPORT_BUCKET"), object_name)

	
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-envPath')
  args = parser.parse_args()

  if args.envPath:
    load_dotenv(dotenv_path=Path(args.envPath))
  
  get_object(os.environ.get("INGRESS_BUCKET"), os.environ.get("S3_KEY"))