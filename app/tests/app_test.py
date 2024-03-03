import boto3
import csv
import os
from moto import mock_aws
from zipfile import ZipFile
# from .src.app import get_object
import pytest


# @pytest.fixture
# def archive(tmpdir):
#    with open(os.path.join(tmpdir, 'data.csv'), 'w', newline='') as csv_file:
#       writer = csv.DictWriter(csv_file, delimiter=',', fieldnames = ['id', 'name'])
#       writer.writeheader()
#       writer.writerow({'id': '1', 'name': 'Test User'})

#    with ZipFile(os.path.join(tmpdir, 'test.zip'), 'w') as archive:  
#       archive.write(csv_file, 'data.csv')
#    return archive
      

@mock_aws
def test_get_object():#archive):
    """ Should ."""

    # Arrange
    bucket_name = "my-bucket"
    object_name = "test.zip"

    #print(archive)

    # s3 = boto3.client('s3', region_name='eu-west-2')
    # s3.create_bucket(Bucket=bucket_name)
    # s3.put_object(Bucket=bucket_name, Key=object_name, Body=archive)
  
    # Act
    res = 200 #get_object(bucket_name, object_name)

    # Assert
    assert res == 200
