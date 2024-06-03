import os
import modules.Utils as Utils
from modules.Parser import Parser
from modules.S3Helper import S3Helper


class App:
    def __init__(self, parser: Parser, ingressS3: S3Helper, reportsS3: S3Helper):
        """ ."""
        self.parser = parser
        self.ingressS3 = ingressS3
        self.reportsS3 = reportsS3

    def generate_report(self, report_file: str, working_folder: str):
        """ ."""

        print(f"Generating reports")

        zip_file = self.ingressS3.download(report_file, working_folder)

        files = Utils.extract_zip(zip_file, "*.csv", working_folder)
        for file in files:
            _, summary = self.parser.parse_file(file)
            upload_filename = Utils.save_json(summary, file, working_folder)
            self.reportsS3.upload(upload_filename, working_folder)

        print(f"Upload complete")

        return len(files)


if __name__ == "__main__":
    """ ."""

    parser = Parser()

    development = os.environ.get('DEVELOPMENT')
    ingressS3 = S3Helper(os.environ.get("INGRESS_BUCKET"), development)
    reportsS3 = S3Helper(os.environ.get("REPORT_BUCKET"), development)

    report_file = os.environ.get("S3_KEY")
    working_folder = ''

    app = App(parser, ingressS3, reportsS3)
    app.generate_report(report_file, working_folder)
