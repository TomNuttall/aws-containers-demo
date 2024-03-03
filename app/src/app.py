import boto3
from pathlib import Path
import os
import csv
from zipfile import ZipFile


def get_object(bucket_name, object_name):
  """ ."""
	
  if not bucket_name or not object_name:
    return
  
  client = boto3.client('s3')
  with open('temp.zip', 'wb') as file:
    client.download_fileobj(bucket_name, object_name, file)
  
  return file

	
if __name__ == "__main__":

  print(os.listdir())
  bucket = os.environ.get("INGRESS_BUCKET")
  print(bucket)
  print(os.environ.get("S3_KEY"))


  with open('data.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, delimiter=',', fieldnames = ['id', 'name'])
    writer.writeheader()
    writer.writerow({'id': '1', 'name': 'Test User'})
    print("CSV CREATED 1")
  print(os.listdir())

  
  # # Create temp folder
  # temp_path = os.path.join(os.getcwd(), "temp")
  # if not os.path.isdir(temp_path):
  #   os.mkdir(temp_path)      
  # os.chdir(temp_path)

  # # 
  # file = get_object(os.environ.get("INGRESS_BUCKET"), os.environ.get("S3_KEY"))
  # print(file)
  
  # with ZipFile('temp.zip', 'r') as archive:  
  #   archive.extractall()docker compose run server npm run test

  #client.upload_file(file_name, os.envrion("REPORT_BUCKET"), object_name)