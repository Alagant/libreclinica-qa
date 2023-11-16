import os, sys, tempfile, time
from src.utils.confluence_helper import ConfluenceHelper
from environment import CONFLUENCE_ACCESS_TOKEN, CONFLUENCE_USERNAME, CONFLUENCE_URL, CONFLUENCE_PAGEID, CONFLUENCE_SPACE_ID

print(f"args {sys.argv},\nos.environ {os.environ}")
message = """##Commit {}\n
{}\n
{}\n
{}""".format(os.environ['source_version'], os.environ['build_id'], os.environ['build_number'], os.environ['commit_message'])
tfile = tempfile.NamedTemporaryFile(mode="w", delete=False)
tfile.write(message)
timestamp = time.strftime("%Y-%m-%dT%H-%M", time.localtime())
print(f"Message written to {tfile.name}")
command=f"pandoc {tfile.name} -f markdown -t pdf -o {tfile.name}.pdf"
print("Mesage: " + message)
print("Execute command: " + command)
os.system(command)
print(f"Uploading to Confluence URL {CONFLUENCE_URL}, with username {CONFLUENCE_USERNAME} and pageid {CONFLUENCE_PAGEID}")
confluence_helper = ConfluenceHelper(confluence_url=CONFLUENCE_URL, username=CONFLUENCE_USERNAME, password=CONFLUENCE_ACCESS_TOKEN)
confluence_helper.upload_pdf_to_confluence(page_id=CONFLUENCE_PAGEID, pdf_file_path=f"{tfile.name}.pdf", pdf_file_name=f"message_{timestamp}.pdf", space=CONFLUENCE_SPACE_ID)
#os.remove(f"{tfile.name}.pdf")
#os.remove(tfile.name)