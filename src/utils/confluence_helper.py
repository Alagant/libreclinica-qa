from atlassian import Confluence
import logging as log

class ConfluenceHelper:
    def __init__(self, confluence_url='', username='', password=''):

        self.confluence = Confluence(
            url=confluence_url,
            username=username,
            password=password)
    
    def upload_pdf_to_confluence(self, page_id, pdf_file_path, pdf_file_name, space):
        log.info(f'Uploading {pdf_file_name} to Confluence...')
        self.confluence.attach_file(filename=pdf_file_path, page_id=page_id, space=space, comment="Uploaded via automated test execution")
        log.info(f'File uploaded successfully at: {self.confluence.url}/wiki/pages/viewpageattachments.action?pageId={page_id}')
