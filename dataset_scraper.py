import requests
from bs4 import BeautifulSoup
from pathlib import Path
from zipfile import ZipFile
import io
import os

xml_data = requests.get("https://divvy-tripdata.s3.amazonaws.com/").content
soup = BeautifulSoup(xml_data, "xml")
# Find the tag/child
raw_files = soup.findAll("Key")
files = dict()

for file in raw_files:
    if file.text.startswith("Divvy"):
        break
    else:
        files.update({str(file.text).strip(): 'https://divvy-tripdata.s3.amazonaws.com/' + str(file.text).strip()})

#grabbing latest 12 filenames
data_files = dict(sorted(files.items(), reverse=True)[:12])

for file_name in data_files.keys():
    path = Path("google_datasets/" + file_name.replace("zip", "csv"))
    if path.is_file() == False:
        r = requests.get(data_files.get(file_name))
        with ZipFile(io.BytesIO(r.content)) as f:
            f.extractall(Path("google_datasets"))
        f.close()

#removing files that do not exist in data_files list
for file_name in os.listdir("google_datasets"):
    if file_name.replace("csv", "zip") not in data_files.keys() and os.path.isdir(Path("google_datasets/" + file_name)) == False:
        path = Path("google_datasets/" + file_name)
        Path.unlink(path, missing_ok=True)
