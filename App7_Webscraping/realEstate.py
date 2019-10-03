import requests
from bs4 import BeautifulSoup
from pandas import DataFrame

base_url = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
l = []
r = requests.get(base_url+"0.html", 
                headers={'User-agent': 'Mozilla/5.0' 
                '(X11; Ubuntu; Linux x86_64; rv:61.0)'
                'Gecko/20100101 Firefox/61.0'})
content = r.content
soup = BeautifulSoup(content, "html.parser")
last_page_nr = soup.find_all("a", {"class": "Page"})[-1].text


for page in range(0, (int(last_page_nr)*10), 10):
    r = requests.get(base_url + str(page) + ".html", 
                    headers={'User-agent': 'Mozilla/5.0' 
                            '(X11; Ubuntu; Linux x86_64; rv:61.0)'
                            'Gecko/20100101 Firefox/61.0'})

    content = r.content
    soup = BeautifulSoup(content, "html.parser")
    property_rows = soup.find_all("div",{"class": "propertyRow"})

   
    for row in property_rows:
        d = {}
        d["Price"] = row.find("h4", {"class": "propPrice"}).text.strip()
        d["Address"] = row.find_all("span", {"class": "propAddressCollapse"})[0].text
        d["Location"] = row.find_all("span", {"class": "propAddressCollapse"})[1].text
        try:
            d["Beds"] = row.find("span", {"class": "infoBed"}).find("b").text
        except AttributeError:
            d["Beds"] = "N/A"
        try:
            d["Area"] = row.find("span", {"class": "infoSqFt"}).find("b").text
        except AttributeError:
            d["Area"] = "N/A"
        try:
            d["Full baths"] = row.find("span", {"class": "infoValueFullBath"}).find("b").text
        except AttributeError:
            d["Full baths"] = "N/A"
        try:
            d["Half baths"] = row.find("span", {"class": "infoValueHalfBath"}).find("b").text
        except AttributeError:
            d["Half baths"] = "N/A"

        for column_group in row.find_all("div", {"class": "columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all(
                                                "span", {"class": "featureGroup"}), 
                                                column_group.find_all(
                                                "span", {"class": "featureName"})):
                if "Lot Size" in feature_group.text:
                    d["Lot size"] = feature_name.text
        l.append(d)

df = DataFrame(l)
df.to_csv("./App7_Webscraping/Output.csv")