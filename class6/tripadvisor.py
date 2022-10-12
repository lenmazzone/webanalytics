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

# tell python where chrome driver is wrt your current working directory
path = "utils/chromedriver"
s = Service(path)
browser = webdriver.Chrome(service=s)

link = "https://www.tripadvisor.com/Attraction_Review-g1187810-d10127777-Reviews-BBQ_Sailing_Trip-Skopelos_Town_Skopelos_Sporades.html"
browser.get(link)

def click_read_more():
    read_more_exists = check_exists_by_xpath("//span[@class='ui_icon caret-down Lvqmo']")
    if read_more_exists:
        element = browser.find_element(By.XPATH, "//span[@class='ui_icon caret-down Lvqmo']")
        browser.execute_script("arguments[0].click();", element)
        time.sleep(5)


# a helper function to check if the button exists on the page
def check_exists_by_xpath(xpath):
    try:
        browser.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


time.sleep(2)
print(check_exists_by_xpath("//span[@class='ui_icon caret-down Lvqmo']"))


# customize how many page reviews you want to scrape
page_num = 5

reviews = []
ratings = []
authors = []

for i in range(0, page_num):

    # expand the reviews
    click_read_more()

    # parse to a soup
    page_source = browser.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    reviews_content = soup.find_all('div', class_='lgfjP Gi z pBVnE MD bZHZM')

    # extract the author, review_text and rating
    for review in reviews_content:
        author = review.find('a', class_='ui_header_link uyyBf').text
        review_text = review.find('q', class_='QewHA H4 _a').text
        rating = review.find('div', class_='Hlmiy F1').span['class'][1][-2]

        # append to our accumulative lists
        reviews.append(review_text)
        ratings.append(rating)
        authors.append(author)

    # use selenium to go to the next page
    if (check_exists_by_xpath('//a[@class="ui_button nav next primary "]')):
        browser.find_element(By.XPATH, '//a[@class="ui_button nav next primary "]').click()
        time.sleep(1)

print(authors)
browser.quit()

data = {
    'reviews':reviews,
    'ratings': ratings,
    'authors':authors
}

df = pd.DataFrame(data)
print(df.shape,"\n", df.head())