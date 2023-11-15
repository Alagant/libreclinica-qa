import os, sys
from src.utils.confluence_helper import ConfluenceHelper
#from src.utils.report import ReportGenerator
from environment import CONFLUENCE_ACCESS_TOKEN, CONFLUENCE_USERNAME, CONFLUENCE_URL, CONFLUENCE_PAGEID, CONFLUENCE_SPACE_ID

print(f"args {sys.argv}")
message = """##Commit {}
{}
{}
{}""".format(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
fileroot = "message"
with open(f"{fileroot}.txt", "w") as tfil:
    tfil.write(message)
print(f"Message written to {tfil.name}")
command=f"pandoc {fileroot}.txt -f markdown -t pdf -o {fileroot}.pdf"
print("Mesage: " + message)
print("Execute command: " + command)
os.system(command)
confluence_helper = ConfluenceHelper(confluence_url=CONFLUENCE_URL, username=CONFLUENCE_USERNAME, password=CONFLUENCE_ACCESS_TOKEN)
confluence_helper.upload_pdf_to_confluence(page_id=CONFLUENCE_PAGEID, pdf_file_path=f"{fileroot}.pdf", pdf_file_name=f"{fileroot}.pdf", space=CONFLUENCE_SPACE_ID)
