import requests
from bs4 import BeautifulSoup

url = requests.get('https://blog.hartleybrody.com/web-scraping-cheat-sheet/').text

soup = BeautifulSoup(url, 'html.parser')

page_title = soup.find('title')
print(page_title)