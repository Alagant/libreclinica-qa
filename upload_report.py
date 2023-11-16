
import glob
import json
import os
import time
from pathlib import Path 
from src.utils.confluence_helper import ConfluenceHelper
from src.utils.report import ReportGenerator
from environment import CONFLUENCE_ACCESS_TOKEN, CONFLUENCE_USERNAME, CONFLUENCE_URL, CONFLUENCE_PAGEID, CONFLUENCE_SPACE_ID


class ReportUploader:
    
    __file_to_upload = None

    def __init__(self):
        pass

    def get_latest_results_file(self):
        
        file = max(glob.glob(os.path.join('allure-results', '*.json')), key=os.path.getctime) #get the latest json file
        return file
    
    def generate_report(self):
        timestamp = time.strftime("%Y-%m-%dT%H-%M", time.localtime())
        file_name = "report-".__add__(timestamp).__add__(".pdf")
        file_path = "reports/".__add__(file_name)

        self.__file_to_upload = file_path
        
        data_results = self.get_latest_results_file()
        with open(data_results, 'r') as test_results:
            test_data = json.load(test_results)

        report_generator = ReportGenerator(filename=file_path)
        report_generator.generate_report(test_data)
    
    def upload_to_confluence(self):
        self.generate_report()

        confluence_helper = ConfluenceHelper(confluence_url=CONFLUENCE_URL, username=CONFLUENCE_USERNAME, password=CONFLUENCE_ACCESS_TOKEN)
        confluence_helper.upload_pdf_to_confluence(page_id=CONFLUENCE_PAGEID, pdf_file_path=self.__file_to_upload, pdf_file_name=Path(self.__file_to_upload).name,
                                                   space=CONFLUENCE_SPACE_ID, comment=f"Automated test report for build {os.environ['build_number']}")


    def run(self):
        self.upload_to_confluence()


report_uploader = ReportUploader()
report_uploader.run()