import pandas as pd


class Parser:

    def parse_file(self, csv_file):
        """ Parse file and return number of rows."""

        csv_data = pd.read_csv(csv_file, delimiter=',')
        summary = csv_data.describe()

        return csv_data.shape[1], summary.to_json()
