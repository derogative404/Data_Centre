import requests
from bs4 import BeautifulSoup
from pathlib import Path
import zipfile

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
    path = Path("google_datasets/" + file_name)
    print(path.is_file())

    # r = requests.get(data_files.get(file_name))
    # with open(file_name, 'wb') as f:
    #     f.write("google_datasets"r.content)

