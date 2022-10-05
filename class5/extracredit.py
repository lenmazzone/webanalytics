import requests  # to get the website

import time  # to force our code to wait a little before re-trying to grab a webpage
import re  # to grab the exact element we need
from bs4 import BeautifulSoup  # to grab the html elements we need

# access the webpage as Chrome
my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
data = []
numPages = 5

for k in range(1, numPages + 1):

    # Give the url of the page
    page = 'https://www.whitehouse.gov/briefing-room/page/' + str(k) + '/'
    # Initialize src to be False
    src = False

    # Now get the page

    # try to scrape 5 times
    for i in range(1, 6):
        try:
            # get url content
            response = requests.get(page, headers=my_headers)
            # get the html content
            src = response.content
            # if we successuflly got the file, break the loop
            break
            # if requests.get() threw an exception, i.e., the attempt to get the response failed
        except:
            print('failed attempt #', i)
            # wait 2 secs before trying again
            time.sleep(2)

    # if we could not get the page
    if not src:
        # couldnt get the page, print that we could not and continue to the next attempt
        print('Could not get page: ', page)
        # move on to the next page
        continue
    else:
        # got the page, let the user know
        print('Successfully got page: ', page)

    soup = BeautifulSoup(src.decode('ascii', 'ignore'), 'lxml')
    articles = soup.findAll('article', {'class': re.compile('news-item')})

    for article in articles:

        # initialize to not found
        article_url = 'NA'
        article_text = 'NA'
        article_date = 'NA'
        article_type = 'NA'

        # find p, grab text, strip() it
        a = article.find('a')
        # if you found it
        if a:
            article_text = a.get_text().strip().replace('\xa0', ' ')
            article_url = a.attrs['href']

        t = article.find('time')
        if t:
            article_date = t.get_text().strip()

        y = article.findAll('a')[1]
        if y:
            article_type = y.get_text().strip()
        # add all the info to the data link
        # if some element hasn't been found, the 'NA' string will be added
        data.append([article_url, article_text, article_date, article_type])

    # always a good idea to take a nap
    time.sleep(2)

print("\n")
for article in data:
    print(article)

with open('white-house.txt', mode ='w', encoding="utf-8") as f:
    for article in data:
        for item in article:
            f.write(item + "\t")
        f.write("\n")

with open('white-house.txt', mode ='r', encoding="utf-8" as f:
    read_articles = f.read().split("\n")
for article in read_articles:
    print(article)