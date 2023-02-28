import requests
from bs4 import BeautifulSoup

# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
#   https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------


with open("templates\\html_example.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    print(soup)

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
type(tag)
# <class 'bs4.element.Tag'>

tag.name = 'block_name'
print(tag.name)
print(tag)
print(tag.attrs)
print(tag['class'])


print ('-----Tag Attributes ----------------')
tag = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser').b
tag['id']
# 'boldest'


tag.attrs
# {'id': 'boldest'}


tag['id'] = 'verybold'
tag['another-attribute'] = 1
tag
# <b another-attribute="1" id="verybold"></b>
print(tag)

#del tag['id']
del tag['another-attribute']
print(tag)
# <b>bold</b>

print(tag['id'])

# KeyError: 'id'
print(tag.get('id'))
# None


# ------------------------------------------------------------------
print ('-----multi-valued attributes ----------------')

css_soup = BeautifulSoup('<p class="body"></p>', 'html.parser')
css_soup.p['class']
# ['body']

css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
css_soup.p['class']
# ['body', 'strikeout']

id_soup = BeautifulSoup('<p id="my id"></p>', 'html.parser')
id_soup.p['id']
# 'my id'

id_soup.p.get_attribute_list('id')
# ["my id"]

rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>', 'html.parser')
rel_soup.a['rel']
# ['index']
rel_soup.a['rel'] = ['index', 'contents']

print(rel_soup.p)
# <p>Back to the <a rel="index contents">homepage</a></p>


no_list_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser', multi_valued_attributes=None)
print(no_list_soup.p['class'])
# 'body strikeout'

# ---------------------------------------------------------------------------------
print ('------XML Parse -------------')
# XML parse
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
xml_soup.p['class']
# 'body strikeout'

class_is_multi= { '*' : 'class'}
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml', multi_valued_attributes=class_is_multi)
xml_soup.p['class']
# ['body', 'strikeout']


# ---------------------------------------------------------------------------------
print ('------Strings-------------')
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
tag.string
# 'Extremely bold'
type(tag.string)
print (type(tag.string))
# <class 'bs4.element.NavigableString'>


unicode_string = str(tag.string)
unicode_string
# 'Extremely bold'
type(unicode_string)
# <type 'str'>

tag.string.replace_with("No longer bold")
tag
# <b class="boldest">No longer bold</b>
 #---------------------------------------------------------------------------------

print('---------Beautiful soup  BS4 ------------')
doc = BeautifulSoup("<document><content/>INSERT FOOTER HERE</document", "xml")
footer = BeautifulSoup("<footer>Here's the footer</footer>", "xml")
doc.find(text="INSERT FOOTER HERE").replace_with(footer)
# 'INSERT FOOTER HERE'
print(doc)
# <?xml version="1.0" encoding="utf-8"?>
# <document><content/><footer>Here's the footer</footer></document>

soup.name
# '[document]'



markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'html.parser')
comment = soup.b.string
type(comment)
# <class 'bs4.element.Comment'>


print(soup.b.prettify())
# <b>
#  <!--Hey, buddy. Want to buy a used parser?-->
# </b>


#------------------------------------------------------------------------
#------------------------------------------------------------------------

with open("templates\\html_example.html") as fp:

    soup = BeautifulSoup(fp, 'html.parser')
    print(soup)

    print(soup.head)
# <head><title>The Dormouse's story</title></head>
    print(soup.title)
# <title>The Dormouse's story</title>
    print(soup.body.b)
# <b>The Dormouse's story</b>
    print(soup.a)
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# ----- find  ------------
    print(soup.find_all('a'))

#------------------------------------------------------------------------
    head_tag = soup.head
    print(head_tag.contents)
# <head><title>The Dormouse's story</title></head>

    title_tag = head_tag.contents[0]
    print(title_tag)
# <title>The Dormouse's story</title>
title_tag.contents
# ['The Dormouse's story']


len(soup.contents)
print (len(soup.contents))
print(soup.contents[0].name)


#text = title_tag.contents[0]
#print(text.contents)
#error because a navigatable string doesn't contain anything


print('----children-----')
for child in title_tag.children:
    print(child)
# The Dormouse's story


# -------------------------------------
print ('----------Descendants----------------')
for child in head_tag.descendants:
    print(child)
# <title>The Dormouse's story</title>
# The Dormouse's story

len(list(soup.children))
# 1
len(list(soup.descendants))
# 26


title_tag.string
# 'The Dormouse's story'


#for string in soup.strings:
#    print(repr(string))
#    '\n'

for string in soup.stripped_strings:
    print(repr(string))


print ('----------Parent----------------')
title_tag = soup.title
title_tag
# <title>The Dormouse's story</title>
print(title_tag.parent)
# <head><title>The Dormouse's story</title></head>
print(title_tag.string.parent)



link = soup.a
print(link)
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
for parent in link.parents:
    print(parent.name)
# p
# body
# html
# [document]



print ('----------Siblings----------------')
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></a>", 'html.parser')
print(sibling_soup.prettify())
#   <a>
#    <b>
#     text1
#    </b>
#    <c>
#     text2
#    </c>
#   </a>


sibling_soup.b.next_sibling
# <c>text2</c>

sibling_soup.c.previous_sibling
# <b>text1</b>

print(sibling_soup.b.previous_sibling)
# None
print(sibling_soup.c.next_sibling)
# None




#Filters
print('--------filters------------')
soup.find_all('b')
# [<b>The Dormouse's story</b>]
print(soup.find_all('b'))

#starting with letter b
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
# body
# b

#containing letter t
for tag in soup.find_all(re.compile("t")):
    print(tag.name)
# html
# title

#finding all a's and b's
soup.find_all(["a", "b"])
# [<b>The Dormouse's story</b>,
#  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]



#finding tags without text strings
for tag in soup.find_all(True):
    print(tag.name)
# html
# head
# title
# body
# p
# b
# p
# a
# a
# a
# p



# ------------------- FUNCTIONS -------------------
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')


print(soup.find_all(has_class_but_no_id))
# [<p class="title"><b>The Dormouse's story</b></p>,
#  <p class="story">Once upon a time there were…bottom of a well.</p>,
#  <p class="story">...</p>]


import re
def not_lacie(href):
    return href and not re.compile("lacie").search(href)

soup.find_all(href=not_lacie)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


soup.find_all(id='link2')
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]


soup.find_all(href=re.compile("elsie"))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

soup.find_all(id=True)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]



#  CAREFUL  CLASS is a reserved word in Python   use CLASS_  instead
soup.find_all("a", class_="sister")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


#different syntax for find_all
soup.find_all("a")
soup("a")

soup.title.find_all(string=True)
soup.title(string=True)




#finding information up in the tree  (backwards into parent)
a_string = soup.find(string="Lacie")
a_string
# 'Lacie'

a_string.find_parents("a")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

a_string.find_parent("p")
# <p class="story">Once upon a time there were three little sisters; and their names were
#  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
#  and they lived at the bottom of a well.</p>

a_string.find_parents("p", class_="title")
# []



#pretty pringing

print(soup.prettify())
print(str(soup.a))

