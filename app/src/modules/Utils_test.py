import boto3
import modules.Utils as Utils
import os
import pytest
from zipfile import ZipFile


# Arrange
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


@pytest.fixture
def extract_folder(tmp_path):
    """ Mock Zip file data."""

    temp_dir = tmp_path / 'extract'
    temp_dir.mkdir()

    return temp_dir


@pytest.fixture
def reports_folder(tmp_path):
    """ Mock Zip file data."""

    temp_dir = tmp_path / 'reports'
    temp_dir.mkdir()

    return temp_dir


def test_extract_zip(zip_file, extract_folder):
    """ It should extract zip and return only csv matches."""

    # Arrange
    matches = '*.csv'

    # Act
    res = Utils.extract_zip(zip_file, matches, extract_folder)

    # Assert
    assert len(res) == 1
    assert os.path.isfile(res[0])


def test_save_json(reports_folder):
    """ It should save a dict to a json file."""

    # Arrange
    filename = "report-jan"
    report_data = {"max": 2}

    # Act
    res = Utils.save_json(report_data, filename, reports_folder)

    # Assert
    assert os.path.isfile(res)
