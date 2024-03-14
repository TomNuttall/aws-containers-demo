import boto3
import csv
import glob
import json
import os
import datetime as dt
from zipfile import ZipFile


def download_zip(bucket_name, object_name):
  """ Download object key from bucket."""

  if not bucket_name or not object_name:
    return None
  
  development = os.environ.get('DEVELOPMENT')
  
  if development:
    access_key = os.environ.get('MINIO_ACCESS_KEY')
    secret_key = os.environ.get('MINIO_SECRET_KEY')

    client = boto3.client('s3', \
                          endpoint_url='http://localhost:9000', \
                          aws_access_key_id=access_key, \
                          aws_secret_access_key=secret_key)
  else:
    client = boto3.client(service_name='s3')

  client.download_file(bucket_name, object_name, object_name)
  return object_name


def extract_files(zip_file, matches):
  """ Extract zip and return csv file paths."""
	
  temp_path = os.path.join(os.getcwd(), "extract")
  if not os.path.isdir(temp_path):
    os.mkdir(temp_path)

  with ZipFile(zip_file, 'r') as fp:  
    fp.extractall(temp_path)

  csv_files = glob.glob(os.path.join(temp_path, matches))
  return csv_files


def parse_file(csv_file):
  """ Parse file and return number of rows."""

  row_count = 0
  with open(csv_file, 'r') as fp:
    reader = csv.DictReader(fp, delimiter=',')
    for row in reader:
      row_count += 1

  return row_count


def upload_report(bucket_name, data):
  """ Upload report data."""

  date_obj = dt.datetime.now()
  with open('data.json', 'w') as fp:
    json.dump(data, fp, indent=2)

  development = os.environ.get('DEVELOPMENT')
  
  if development:
    access_key = os.environ.get('MINIO_ACCESS_KEY')
    secret_key = os.environ.get('MINIO_SECRET_KEY')

    client = boto3.client('s3', \
                          endpoint_url='http://localhost:9000', \
                          aws_access_key_id=access_key, \
                          aws_secret_access_key=secret_key)
  else:
    client = boto3.client('s3')

  client.upload_file('data.json', bucket_name, f'report_{date_obj.strftime("%d/%m/%Y")}.json')


if __name__ == "__main__":
  """ ."""
  
  ingress_bucket = os.environ.get("INGRESS_BUCKET")
  filename = os.environ.get("S3_KEY")

  zip_file = download_zip(ingress_bucket, filename)
  files = extract_files(zip_file, "*.csv")
  for file in files:
    count = parse_file(file)
    print(f"Parsed: {file} - {count}")