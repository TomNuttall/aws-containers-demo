import glob
import os
import json
import datetime as dt
from zipfile import ZipFile


def extract_zip(zip_filepath: str, matches: str, temp_path: str) -> list[str]:
    """ Extract zip and return csv file paths."""

    extract_path = os.path.join(temp_path, "extract")
    if not os.path.isdir(extract_path):
        os.mkdir(extract_path)

    with ZipFile(zip_filepath, 'r') as fp:
        fp.extractall(extract_path)

    csv_files = glob.glob(os.path.join(extract_path, matches))
    return csv_files


def save_json(data: dict, file: str, temp_path: str) -> str:
    """ Save dictionary data to a file."""

    filename, _ = os.path.splitext(os.path.basename(file))

    date_obj = dt.datetime.now()
    upload_filename = f'{filename}_{date_obj.strftime("%d-%m-%Y")}.json'

    reports_path = os.path.join(temp_path, "reports")
    if not os.path.isdir(reports_path):
        os.mkdir(reports_path)

    report_filename = os.path.join(reports_path, upload_filename)
    with open(report_filename, 'w') as fp:
        json.dump(data, fp, indent=2)

    return report_filename
