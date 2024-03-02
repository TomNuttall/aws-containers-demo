import argparse
import boto3
from dotenv import load_dotenv
from pathlib import Path
import shutil
import os
from zipfile import ZipFile


def setupEnv():
  """ ."""

  parser = argparse.ArgumentParser()
  parser.add_argument('-envPath')
  args = parser.parse_args()

  if args.envPath:
    load_dotenv(dotenv_path=Path(args.envPath))


def get_object(bucket_name, object_name):
  """ ."""
	
  if not bucket_name or not object_name:
    return
  
  client = boto3.client('s3')
  with open('temp.zip', 'wb') as file:
    client.download_fileobj(bucket_name, object_name, file)

  with ZipFile('temp.zip', 'r') as archive:  
    archive.extractall()
  os.remove('temp.zip')

  print(os.listdir())

	
if __name__ == "__main__":
  setupEnv()
  
  # Create temp folder
  temp_path = os.path.join(os.getcwd(), "temp")
  if not os.path.isdir(temp_path):
    os.mkdir(temp_path)      
  os.chdir(temp_path)

  # 
  get_object(os.environ.get("INGRESS_BUCKET"), os.environ.get("S3_KEY"))

  # Cleanup
  shutil.rmtree(temp_path)


  #client.upload_file(file_name, os.envrion("REPORT_BUCKET"), object_name)