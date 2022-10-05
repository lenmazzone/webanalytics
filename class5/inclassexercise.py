# 1. importing useful libraries

import requests  # to get the website
import time  # to force our code to wait a little before re-trying to grab a webpage
import re  # to grab the exact element we need
from bs4 import BeautifulSoup  # to grab the html elements we need

# create an empty list
data = []
# access the webpage as Chrome
my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
# Give the url of the page
page = 'https://www.whitehouse.gov/briefing-room/page/1/'
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
        # if we successfully got the file, break the loop
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
else:
    # got the page, let the user know
    print('Successfully got page: ', page)

# 1. decode('ascii', 'ignore') will turn weird characters to more easy-to-work-with characters in our html file
# 2. 'lxml' tells the beautiful soup library what kind of data the src variable contains (an html page)

soup = BeautifulSoup(src.decode('ascii', 'ignore'), 'lxml')

links = soup.find_all("a")
#print(links[1])

#print(re.findall('<a .+</a>', response.text ))

articles = soup.findAll('article')
#print(articles[0].prettify())

articles = soup.findAll('article', {'class':re.compile('news-item')})
#print(len(articles))

article = articles[0]
#print(article)

a = article.find('a')
#print(a)

article_text = a.get_text().strip().replace('\xa0', ' ')
#print(article_text)

article_url = a.attrs['href']
#print(article_url)

print('url   = '+ article_url)
print('text  = '+ article_text)

data = []

articles = soup.findAll('article', {'class': re.compile('news-item')})

for article in articles:
    # find a, grab text, strip() it
    a = article.find('a')
    article_text = a.get_text().strip().replace('\xa0', ' ')

    # and get the url too
    article_url = a.attrs['href']

    # add all the info to the data link
    data.append([article_url, article_text])

for article in data:
    print(article)
print("\n")
data = []

articles = soup.findAll('article', {'class': re.compile('news-item')})

for article in articles:

    # initialize to not found
    article_url = 'NA'
    article_text = 'NA'

    # find p, grab text, strip() it
    a = article.find('a')

    # if you found it
    if a:
        article_text = a.get_text().strip().replace('\xa0', ' ')
        article_url = a.attrs['href']

    # add all the info to the data link
    # if some element hasn't been found, the 'NA' string will be added
    data.append([article_url, article_text])

for article in data:
    print(article)
print("\n")
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

        # find p, grab text, strip() it
        a = article.find('a')

        # if you found it
        if a:
            article_text = a.get_text().strip().replace('\xa0', ' ')
            article_url = a.attrs['href']

        # add all the info to the data link
        # if some element hasn't been found, the 'NA' string will be added
        data.append([article_url, article_text])

    # always a good idea to take a nap
    time.sleep(2)

print("\n")
for article in data:
        print(article)