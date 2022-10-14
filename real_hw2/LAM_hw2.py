import time
import pandas as pd
from bs4 import BeautifulSoup
# pip install selenium if you need to install it -- you also need to download some drivers!
from selenium import webdriver
# Service is an object that manages the starting and stopping of the ChromeDriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
# The By class is used to locate elements within a document
from selenium.webdriver.common.by import By

path = "../utils/chromedriver"
s = Service(path)
browser = webdriver.Chrome(service=s)

movie = "gangs_of_new_york"
pageNum = 3


link = f"https://www.rottentomatoes.com/m/{movie}/reviews"
browser.get(link)
time.sleep(4)
