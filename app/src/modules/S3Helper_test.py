import boto3
import os
import pytest
from modules.S3Helper import S3Helper
from moto import mock_aws
from zipfile import ZipFile

ZIP_FILENAME = "test.zip"
REPORT_FILENAME = 'report_01-01-2024.json'


@pytest.fixture
def zip_file(tmp_path):
    """ Mock Zip file data."""

    temp_dir = tmp_path / 'zip'
    temp_dir.mkdir()

    csv_fp = temp_dir / 'data.csv'
    csv_fp.touch()

    txt_fp = temp_dir / 'text.txt'
    txt_fp.touch()

    zfp = temp_dir / ZIP_FILENAME
    zfp.touch()

    with ZipFile(zfp, 'w') as zip_file:
        zip_file.write(csv_fp, 'data.csv')
        zip_file.write(txt_fp, 'text.txt')
    return zfp


@pytest.fixture
def download_folder(tmp_path):
    """ Mock Zip file data."""

    temp_dir = tmp_path / 'download'
    temp_dir.mkdir()

    return temp_dir


@pytest.fixture
def report_file(tmp_path):
    """ Mock json file data."""

    json_fp = tmp_path / REPORT_FILENAME
    json_fp.touch()
    return json_fp


@mock_aws
def test_download_zip(zip_file, download_folder):
    """ It should download file and return the zip file."""

    # Arrange
    bucket_name = "ingress-bucket"
    object_name = ZIP_FILENAME

    s3 = boto3.client('s3', region_name='eu-west-2')
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
                     'LocationConstraint': 'eu-west-2'})
    with open(zip_file, 'rb') as fp:
        s3.put_object(Bucket=bucket_name, Key=object_name, Body=fp)

    bucket = S3Helper(bucket_name, False)

    # Act
    res = bucket.download(object_name, download_folder)

    # Assert
    assert os.path.isfile(res)


@mock_aws
def test_upload_report(report_file):
    """ It should upload a file to the report bucket."""

    # Arrange
    bucket_name = "report-bucket"

    s3 = boto3.client('s3', region_name='eu-west-2')
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
                     'LocationConstraint': 'eu-west-2'})

    bucket = S3Helper(bucket_name, False)

    # Act
    head, tail = os.path.split(report_file)
    bucket.upload(tail, head)

    res = s3.list_objects(Bucket=bucket_name)

    # Assert
    assert len(res['Contents']) == 1
