import csv
import pytest
from modules.Parser import Parser


@pytest.fixture
def csv_file(tmp_path):
    """ Mock CSV file data."""

    fp = tmp_path / 'data.csv'
    with open(fp, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, delimiter=',',
                                fieldnames=['id', 'name'])
        writer.writeheader()
        writer.writerow({'id': '1', 'name': 'Test User 1'})
        writer.writerow({'id': '2', 'name': 'Test User 2'})
    return fp


def test_parse_file(csv_file):
    """ It should read the csv file and return number of rows."""

    # Arrange
    parser = Parser()

    # Act
    count, summary = parser.parse_file(csv_file)

    # Assert
    assert count == 2
