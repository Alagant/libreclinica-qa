import os, sys, tempfile, time
from src.utils.confluence_helper import ConfluenceHelper
from environment import CONFLUENCE_ACCESS_TOKEN, CONFLUENCE_USERNAME, CONFLUENCE_URL, CONFLUENCE_PAGE_ID, CONFLUENCE_SPACE_ID

print(f"args {sys.argv},\nos.environ {os.environ}")
branch = os.environ.get('branch', '(unknown branch)')
message = f"""#Commit {os.environ['source_version']}\n
Branch: {branch}\n
Build ID: {os.environ['build_id']}\n
Build number: {os.environ['build_number']}\n
{os.environ['commit_message']}"""
tfile = tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".md")
tfile.write(message)
tfile.close()
timestamp = time.strftime("%Y-%m-%dT%H-%M", time.localtime())
print(f"Commit message written to {tfile.name}")
pdf_filename= f"commit_message_{timestamp}_{branch}.pdf"
pdf_file_path = os.path.join("/tmp", pdf_filename)
command=f"pandoc {tfile.name} -f markdown -t pdf -o {pdf_file_path} --pdf-engine=pdflatex"
print("Message: " + message)
print("Execute command: " + command)
os.system(command)
os.system(f"ls -l {tfile.name}*")
print(f"Uploading to Confluence URL {CONFLUENCE_URL}, with username {CONFLUENCE_USERNAME} and pageid {CONFLUENCE_PAGE_ID} the PDF file {pdf_file_path}")
confluence_helper = ConfluenceHelper(confluence_url=CONFLUENCE_URL, username=CONFLUENCE_USERNAME, password=CONFLUENCE_ACCESS_TOKEN)
try:
    confluence_helper.upload_pdf_to_confluence(page_id=CONFLUENCE_PAGE_ID, pdf_file_path=pdf_file_path,
                                           pdf_file_name=pdf_filename, space=CONFLUENCE_SPACE_ID,
                                           comment=f"Build {os.environ['build_number']} description")
except Exception as e:
    print(f"Exception {e} while uploading to Confluence")
    raise e
finally:
    print("Removing temporary files")
    os.remove(pdf_file_path)
    os.remove(tfile.name)