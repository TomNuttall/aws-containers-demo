import boto3
import csv
import pytest
from moto import mock_aws
from zipfile import ZipFile
from src.app import download_zip, extract_files, parse_file, upload_report


# Arrange
@pytest.fixture
def csv_file(tmp_path): 
  """ Mock CSV file data."""

  temp_dir = tmp_path / 'csv'  
  temp_dir.mkdir()  
  
  fp = temp_dir / 'data.csv'
  with open(fp, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, delimiter=',', fieldnames = ['id', 'name'])
    writer.writeheader()
    writer.writerow({'id': '1', 'name': 'Test User 1'})
    writer.writerow({'id': '2', 'name': 'Test User 2'})
  return fp


@pytest.fixture
def zip_file(tmp_path):
  """ Mock Zip file data."""

  temp_dir = tmp_path / 'zip'  
  temp_dir.mkdir()  

  csv_fp = temp_dir / 'data.csv'
  csv_fp.touch()

  txt_fp = temp_dir / 'text.txt'
  txt_fp.touch()

  zfp = temp_dir / 'test.zip'
  zfp.touch()
  
  with ZipFile(zfp, 'w') as zip_file:  
    zip_file.write(csv_fp, 'data.csv')
    zip_file.write(txt_fp, 'text.txt')
  return zfp
      

@mock_aws
def test_download_zip(zip_file):
    """ It should download file and return the zip file."""

    # Arrange
    bucket_name = "ingress-bucket"
    object_name = "test.zip"

    s3 = boto3.client('s3', region_name='eu-west-2')
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})
    with open(zip_file, 'rb') as fp:
      s3.put_object(Bucket=bucket_name, Key=object_name, Body=fp)
  
    # Act
    res = download_zip(bucket_name, object_name)

    # Assert
    assert res == object_name


def test_extract_files(zip_file):
    """ It should extract zip and return csv matches."""

    # Arrange
    matches = '*.csv'
  
    # Act
    res = extract_files(zip_file, matches)

    # Assert
    assert len(res) == 1


def test_parse_file(csv_file):
    """ It should read the csv file and return number of rows."""

    # Arrange
  
    # Act
    res = parse_file(csv_file)

    # Assert
    assert res == 2


@mock_aws
def test_upload_report():
    """ It should upload a file to the report bucket."""

    # Arrange
    bucket_name = "report-bucket"

    s3 = boto3.client('s3', region_name='eu-west-2')
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})
  
    report_data = { "rows": 2 }

    # Act
    upload_report(bucket_name, report_data)

    res = s3.list_objects(Bucket=bucket_name)

    # Assert
    assert len(res['Contents']) == 1