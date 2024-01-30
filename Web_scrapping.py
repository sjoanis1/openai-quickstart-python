import requests
import re
from bs4 import BeautifulSoup





##from Html file
#with open("templates\\html_example.html") as fp:
#    soup = BeautifulSoup(fp, 'html.parser')
#     print(soup.prettify())

#-------------------------------------------------------------------------------
# Get the webpage
url = 'https://www.strasburgfire.org/'
page = requests.get(url)


# Create a BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
#print(soup.text)


#find all tags
#for tag in soup.find_all(True):
#    print(tag.name)


print('----------ID---------------')
id = soup.find(id= 'footer')
print(id.text)

print('----------Class---------------')
my_classes = soup.find(class_ = 'three-column-no-wrap__first')
print(my_classes.text)

print('----------tag---------------')
tags = soup.find_all(['p'])
for soups in tags:
    print(soups.text)




 #----------------------------------
 # https://www.makeuseof.com/beautiful-soup-tutorial/
 #  
 #creating a function looking for prices of shirts 
#import pandas as pd
#class scrapeit:
# try:
# def scrape(website=None, tag1=None, id1=None, tag2=None, id2=None):

# if not (website and tag1 and id1 and tag2 and id2)==None: 
# try:
# page = requests.get(website)
# soup = BeautifulSoup(page.content, 'html.parser')

# infotag1 = soup.find_all(tag1, id1)
# infotag2 = soup.find_all(tag2, id2) 
# priced = [prices.text for prices in infotag1]
# shirt = [shirts.text for shirts in infotag2]
# data = {
# 'Price':priced, 
# 'Shirt_name':shirt}
# info = pd.DataFrame(data, columns=['Price', 'Shirt_name'])
# print(info)
# except:
# print('Not successful')
# else:
# print('Oops! Please enter a website, two tags and thier corresponding ids')
# except:
# print('Not successful!')


#Function can be imported to a different module
#rom scraper_module import scrapeit
#scrapeit.scrape('URL', 'price_tag', 'price_id', 'shirt_tag', 'shirt_id')
