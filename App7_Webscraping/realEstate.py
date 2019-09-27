import requests
from bs4 import BeautifulSoup


r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", 
                 headers={'User-agent': 'Mozilla/5.0' 
                          '(X11; Ubuntu; Linux x86_64; rv:61.0)'
                          'Gecko/20100101 Firefox/61.0'})

content = r.content
soup = BeautifulSoup(content, "html.parser")

property_rows = soup.find_all("div",{"class": "propertyRow"})

for row in property_rows:
    price = row.find("h4", {"class": "propPrice"}).text.strip()
    address = row.find_all("span", {"class": "propAddressCollapse"})
    try:
        beds = row.find("span", {"class": "infoBed"}).find("b").text
    except AttributeError:
        beds = "N/A"
    try:
        area = row.find("span", {"class": "infoSqFt"}).find("b").text
    except AttributeError:
        area = "N/A"
    try:
        full_baths = row.find("span", {"class": "infoValueFullBath"}).find("b").text
    except AttributeError:
        full_baths = "N/A"
    try:
        half_baths = row.find("span", {"class": "infoValueHalfBath"}).find("b").text
    except AttributeError:
        half_baths = "N/A"

    print(price, address[0].text, address[1].text, beds, area, full_baths, half_baths, "\n")