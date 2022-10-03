import re
import time

import requests as requests

url = "http://www.apostolos-filippas.com/"
my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

success = False

# try 5 times
for i in range(1, 6):
    try:
        # use the browser to access the url
        response = requests.get(url, headers=my_headers)
        # if an error does not occur, set success
        success = True
        print('Successfully retrieved the webpage!')
        # we got the file, break the loop
        break
    except:
        # if we got an exception, the attempt to get the response failed
        print('failed attempt', i)
        # wait for 2 seconds before you go to the next iteration of the loop
        time.sleep(2)

print(response.headers)

text = response.text
print(text)

papers = re.findall('papers/.+>(.+)<', text)
print(papers)

classes = re.findall('<li>.20.+---.(.+),', text)

print(classes)
unique_classes = list()
for item in classes:
    if item not in unique_classes:
        unique_classes.append(item)

print(unique_classes)

