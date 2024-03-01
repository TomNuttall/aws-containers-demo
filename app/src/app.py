import boto3
import os
import argparse
from dotenv import load_dotenv
from pathlib import Path


def list_bucket(bucket_name):
  """ ."""
	
  client = boto3.client('s3')
  response = client.list_objects(Bucket=bucket_name)
  print(response)

  # for item in response.get('Contents'):
  #   print(item)
	

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-envPath')
  args = parser.parse_args()

  if args.envPath:
    load_dotenv(dotenv_path=Path(args.envPath))

  bucket_name = os.environ.get("INGRESS_BUCKET")
  if bucket_name:
    list_bucket(bucket_name)