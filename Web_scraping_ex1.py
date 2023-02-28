import requests
import pandas as pd
from bs4 import BeautifulSoup




# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Beautiful soup
# ----------------------------------------------------------------------------------------
#   https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
#with open("templates\\html_example.html") as fp:
#    soup = BeautifulSoup(fp, 'html.parser')
#     print(soup.prettify())

# ----------------------------------------------------------------------------------------
##soup = BeautifulSoup(requests.get(url).content, 'html.parser')



#-------------------------------------------------------------------------------
# Get the webpage
#url = 'https://www.strasburgfire.org/'
#page = requests.get(url)

## Create a BeautifulSoup object
#soup = BeautifulSoup(page.text, 'html.parser')
#print(soup)

## Find the fire chief
#fire_chief = soup.find('div', class_='fire')

## Print the fire chief
#print(fire_chief)  
  


#-------------------------------------------------------------------------------



#url = "https://www.sjperformancecoach.com/about-us"
#soup = BeautifulSoup(requests.get(url).content, 'html.parser')
#print(soup)

#psoup = soup.prettify()



#head_tag = soup.head
#print(head_tag.contents)

#for child in head_tag.descendants:
#    print(child)

#-------------------------------------------------------------------------------
#for child in head_tag.descendants:
#    print(child)


#title_tag = head_tag.contents[0]
#print(title_tag)


#links = psoup.find_all("a")
#print(links)
#print(soup.get_attribute_list("a"))
#print(soup)




#for link in links:
#    if "stephane" in link.get("href") and 'Joanis' in link.text:
#        print(link)
        
        
       # print "<a href='%s'>%s</a>" %(link.get("href"), link.text)
























# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
#url = "https://www.bseindia.com/corporates/Forth_Results.aspx"
#headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
#soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')


#page = 1
#all_data = []
#while True:
#    print(page)
#    rows = soup.select('.TTRow')
#    print('rows =', rows)
#    if not rows:
#        break

#    # print some data to screen:
#    for tr in rows:
#        print(tr.get_text(strip=True, separator=' '))

#    # to get correct page, you have to do POST request with correct data
#    # the data is located in <input name="..." value=".."> tags
#    d = {}
#    for i in soup.select('input'):
#        d[i['name']] = i.get('value', '')

#    # some data parameters needs to be deleted:
#    if 'ctl00$ContentPlaceHolder1$btnSubmit' in d:
#        del d['ctl00$ContentPlaceHolder1$btnSubmit']


#    # set correct page:
#    page += 1
#    d['__EVENTTARGET'] = 'ctl00$ContentPlaceHolder1$gvData'
#    d['__EVENTARGUMENT'] = 'Page${}'.format(page)

#    soup = BeautifulSoup(requests.post(url, headers=headers, data=d).content, 'html.parser')

#df = pd.DataFrame(all_data)
#print(df)
#df.to_csv('data.csv')