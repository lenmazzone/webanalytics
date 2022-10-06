from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

path = "./utils/chromedriver"
s=Service(path)

browser = webdriver.Chrome(service=s)

browser.get("http://www.apostolos-filippas.com")

browser.quit()