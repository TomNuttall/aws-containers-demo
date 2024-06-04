import boto3
import csv
import pytest
from app import App
from parser.Parser import Parser
from modules.S3Helper import S3Helper
from moto import mock_aws
from zipfile import ZipFile

ZIP_FILENAME = "test.zip"
INGRESS_BUCKET = "ingress-bucket"
REPORT_BUCKET = "report-bucket"


# Arrange
@pytest.fixture
def zip_file(tmp_path):
    """ Mock Zip file data."""

    temp_dir = tmp_path / 'zip'
    temp_dir.mkdir()

    csv_fp = temp_dir / 'data.csv'
    with open(csv_fp, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, delimiter=',',
                                fieldnames=['id', 'name'])
        writer.writeheader()
        writer.writerow({'id': '1', 'name': 'Test User 1'})
        writer.writerow({'id': '2', 'name': 'Test User 2'})

    txt_fp = temp_dir / 'text.txt'
    txt_fp.touch()

    zfp = temp_dir / 'test.zip'
    zfp.touch()

    with ZipFile(zfp, 'w') as zip_file:
        zip_file.write(csv_fp, 'data.csv')
        zip_file.write(txt_fp, 'text.txt')
    return zfp


@pytest.fixture
def temp_folder(tmp_path):
    """ Mock temp folder."""

    temp_dir = tmp_path / 'temp'
    temp_dir.mkdir()
    return temp_dir


@mock_aws
def test_generate_report(zip_file, temp_folder):
    """ It should create report from csv file."""

    # Arrange
    s3 = boto3.client('s3', region_name='eu-west-2')
    s3.create_bucket(Bucket=INGRESS_BUCKET, CreateBucketConfiguration={
                     'LocationConstraint': 'eu-west-2'})
    s3.create_bucket(Bucket=REPORT_BUCKET, CreateBucketConfiguration={
                     'LocationConstraint': 'eu-west-2'})
    with open(zip_file, 'rb') as fp:
        s3.put_object(Bucket=INGRESS_BUCKET, Key=ZIP_FILENAME, Body=fp)

    parser = Parser()
    ingressS3 = S3Helper(INGRESS_BUCKET, False)
    reportsS3 = S3Helper(REPORT_BUCKET, False)

    report_file = ZIP_FILENAME
    working_folder = temp_folder

    app = App(parser, ingressS3, reportsS3)

    # Act
    res = app.generate_report(report_file, working_folder)

    # Assert
    assert res == 1
