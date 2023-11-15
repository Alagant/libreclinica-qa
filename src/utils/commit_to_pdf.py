import os, sys
message = """##{}
{}
{}""".format(sys.argv[1], sys.argv[2], sys.argv[3])
fileroot = "message"
with open(f"{fileroot}.txt", "w") as tfil:
    tfil.write(message)
print(f"Message written to {tfil.name}")
command=f"pandoc {fileroot}.txt -f markdown -t pdf -o {fileroot}.pdf"
print("Execute command: " + command)
os.system(command)