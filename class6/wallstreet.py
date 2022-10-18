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

link = "https://www.tripadvisor.com/Attraction_Review-g60763-d136051-Reviews-Wall_Street-New_York_City_New_York.html"
browser.get(link)
time.sleep(4)


def click_read_more():
    read_more_exists = check_exists_by_xpath("//span[@class='biGQs _P XWJSj Wb']")
    print(f"{read_more_exists} = read_more_exists")
    if read_more_exists:
        element = browser.find_element(By.XPATH, "//span[@class='biGQs _P XWJSj Wb']")
        browser.execute_script("arguments[0].click();", element)
        time.sleep(5)


# a helper function to check if the button exists on the page
def check_exists_by_xpath(xpath):
    try:
        browser.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


browser.find_element(By.CSS_SELECTOR,
                     "#tab-data-qa-reviews-0 > div > div.LXdgT > span > div > div.JEtPQ > div > div > span:nth-child(1) > span > button").click()
browser.find_element(By.CSS_SELECTOR,
                     'body > div.HyAcm.D.t._U.s.l.Za.f > div > div.YmElR._T > div > span:nth-child(4) > span > button:nth-child(2)').click()
browser.find_element(By.CSS_SELECTOR,
                     'body > div.HyAcm.D.t._U.s.l.Za.f > div > div.HllFM.F- > div > div.HyFLq.ceyRp > button').click()

# customize how many page reviews you want to scrape
page_num = 5

reviews = []
ratings = []
authors = []
dates = []

for i in range(0, page_num):

    # Make sure all the reviews are exposed
    if check_exists_by_xpath('//button[@class="rmyCe _G B- z _S c Wc wSSLS roAGK w pexOo QHaGY"]'):
        browser.find_element(By.CSS_SELECTOR, '#tab-data-qa-reviews-0 > div > div.LbPSX > button').click()
        print("see more button clicked")
        time.sleep(1)

    # expand the reviews
    click_read_more()

    # parse to a soup
    page_source = browser.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    reviews_content = soup.find_all('div', class_='_c')
    # print(reviews_content)

    # extract the author, review_text and rating
    for review in reviews_content:
        author = review.find('span', class_='biGQs _P fiohW fOtGX').a.text
        review_text = review.find('div', class_='biGQs _P pZUbB KxBGd').span.text
        rating = review.find('svg', class_='UctUV d H0').get('aria-label')
        date = review.find('div', class_='biGQs _P pZUbB ncFvv osNWb').text

        # print(author,"\n",rating,"\n",review_text, "\n",date)
        # append to our accumulative lists
        reviews.append(review_text)
        ratings.append(rating.strip(' bubbles'))
        authors.append(author)
        dates.append(date.strip('Written'))

    # use selenium to go to the next page
    if check_exists_by_xpath('//*[@id="tab-data-qa-reviews-0"]/div/div[5]/div[11]/div[1]/div/div[1]/div[2]/div/a'):
        browser.find_element(By.CSS_SELECTOR,
                             '#tab-data-qa-reviews-0 > div > div.LbPSX > div:nth-child(11) > div:nth-child(2) > div > div.OvVFl.j > div.xkSty > div > a').click()
        print("going to a new page")
        time.sleep(1)
    else:
        break

# print(authors)
browser.quit()

data = {
    'reviews': reviews,
    'ratings': ratings,
    'authors': authors,
    'dates': dates
}

df = pd.DataFrame(data, columns=['reviews', 'ratings', 'authors', 'dates'])
print(df.shape,"\n", df.head(), "\n")

df.sort_values(by=['ratings', 'dates'], inplace=True, ascending=False)

with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(df)

# At least from a casual analysis, I don't see a strong relationship between review amounts and dates
