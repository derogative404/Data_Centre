# import requests
# from bs4 import BeautifulSoup
#
# # specify the URL of the archive here
# archive_url = "https://divvy-tripdata.s3.amazonaws.com/index.html"
#
#
# def get_video_links():
#     # create response object
#     r = requests.get(archive_url)
#     # create beautiful-soup object
#     soup = BeautifulSoup(r.content, 'html5lib')
#     # find all links on web-page
#     # links = soup.findAll('tbody')
#     table = soup.findAll(lambda tag: tag.name == 'tbody' and tag.has_attr('id') and tag['id'] == "tbody-content")
#     print(table)
#     # filter the link ending with .mp4
#     video_links = [archive_url + link['href'] for link in links if link['href'].endswith('zip')]
#
#     return video_links
#
# x = get_video_links()
# print(x)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# instantiate options
options = webdriver.ChromeOptions()

# run browser in headless mode
options.headless = True

# instantiate driver
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), options=options)

# load website
url = 'https://divvy-tripdata.s3.amazonaws.com/index.html'

# get the entire website content
driver.get(url)