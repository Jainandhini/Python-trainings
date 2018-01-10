import requests
from bs4 import BeautifulSoup


url=r'https://jaiescribe.wordpress.com/'

def inspect_blog(url):
    source_code=requests.get(url)
    plain_text=source_code.text
    soup=BeautifulSoup(plain_text,"html.parser")
    for l in soup.findAll('h1',{'class':'entry-title'}):
        print(l.string)

inspect_blog(url)





