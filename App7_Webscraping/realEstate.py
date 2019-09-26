import requests
from bs4 import BeautifulSoup


r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", 
                 headers={'User-agent': 'Mozilla/5.0' 
                          '(X11; Ubuntu; Linux x86_64; rv:61.0)'
                          'Gecko/20100101 Firefox/61.0'})

content = r.content
soup = BeautifulSoup(content, "html.parser")

property_rows = soup.find_all("div",{"class": "propertyRow"})
prices = property_rows[0].find("h4", {"class": "propPrice"}).text.replace("\n", "").replace(" ", "")
print(prices)