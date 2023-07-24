import requests
from bs4 import BeautifulSoup
import sys

url = "https://www.hackerearth.com/"

try :
    req = requests.get(url)
except Exception as e:
    print("Error !!!!",e)
    
p1 = req.content
p2 = req.links
p3 = req.text
p4 = req.cookies
p5 = req.headers
p6 = req.history


soup = BeautifulSoup(p1, 'html.parser')
'''
html script ko badiya way me lik dega
print(soup.prettify)
'''


'''
sirf text print karega 
print(soup.text)
'''

'''
returns 1 st para
print(soup.find('p'))
'''

'''
returns 1 st anchor tag
print(soup.find('a'))
'''


'''
returns all para
print(soup.find_all('p'))
'''

'''
returns title
print(soup.title)
'''


'''
return beautifulsoup

print(type(soup))
'''

'''
return tag

print(type(soup.title))
'''

'''
returns navigation string
print(type(soup.title.string))
'''


'''
return  response
print(type(req))
'''