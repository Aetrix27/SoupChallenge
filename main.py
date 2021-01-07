import requests
import re
from bs4 import BeautifulSoup as bs

# Load the webpage content
r = requests.get("https://champagneproxy.github.io/webscraping/example2.html")

# Convert to a beautiful soup object
soup = bs(r.content, features="html.parser")

# Pretty prints out our html
print(soup.prettify())

links = soup.select("a")

for link in links:
  print(link['href'])

headers_re = soup.find_all("p", string=re.compile("is"))
print(headers_re)

