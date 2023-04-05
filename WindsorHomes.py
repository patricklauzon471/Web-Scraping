from bs4 import BeautifulSoup
import requests

url = "https://www.realtor.ca/on/windsor/condos-for-sale"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', {'class':"listingCard"})

for list in lists:
    Price = list.find('div', class_ = "listingCardPrice")
    Address = list.find('div', class_ = "listingCardAddress")
    info = [Price, Address]
    print(info)