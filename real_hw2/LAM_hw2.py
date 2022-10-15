import time

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def check_exists_by_xpath(xpath):
    try:
        browser.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


path = "../utils/chromedriver_linux"
s = Service(path)
browser = webdriver.Chrome(service=s)

default_movie = 'gangs_of_new_york'
default_pageNum = 3


movie = input(f'Enter a movie title (defaults to {default_movie}):').lower().replace(' ', '_') or default_movie
pageNum = int(
    input(f'How many pages of reviews do you want to collect? (defaults to {default_pageNum})') or default_pageNum)

# NB, this will not work if there are multiple movies with the same title
link = f"https://www.rottentomatoes.com/m/{movie}/reviews"
browser.get(link)
time.sleep(4)

critics = []
ratings = []
sources = []
contents = []
dates = []

for i in range(pageNum):
    page_source = browser.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    reviews_content = soup.find_all('div', class_='row review_table_row')
    # print(f" reviews content: {reviews_content}")

    for review in reviews_content:
        critic = review.find('a', {"data-qa": "review-critic-link"}).text or "NA"
        rating = review.find("div", class_='review_icon')['class'].pop() or "NA"
        source = review.find('em', {"data-qa": "review-critic-publication"}).text or "NA"
        content = review.find('div', {"data-qa": "review-text"}).text.strip() or "NA"
        date = review.find('div', {"data-qa": "review-date"}).text.strip() or "NA"

        # print(critic, rating, source, content, date, type(rating))

        critics.append(critic)
        ratings.append(rating)
        sources.append(source)
        contents.append(content)
        dates.append(date)

    if check_exists_by_xpath('//*[@id="content"]/div/div/div/nav[1]/button[2]'):
        browser.find_element(By.CSS_SELECTOR,
                             '#content > div > div > div > nav:nth-child(1) > button.js-prev-next-paging-next.btn.prev-next-paging__button.prev-next-paging__button-right').click()
        print("going to a new page")
        time.sleep(1)
    else:
        break
browser.quit()

data = {
    'critics': critics,
    'ratings': ratings,
    'sources': sources,
    'contents': contents,
    'dates': dates
}
df = pd.DataFrame(data)
print(df.shape, "\n", df.head())

with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(df)

print("Writing to file")
df.to_csv(f'./reviews/leonard_mazzone_{movie}.txt', header=None, index=None, sep="\t", mode='a')
print("Done writing")

with open(f'./reviews/leonard_mazzone_{movie}.txt', mode='r', encoding="utf-8") as f:
    read_reviews = f.read().split("\n")

print("Printing readout of files", read_reviews)

for review in read_reviews:
    print(review)
