#This program retrieves the elite trade in value for the xbox games.

import re
import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup


print("Eilte Trade in Values")
with open('realXboxOneUrls.txt') as inf:
    urls = (line.strip() for line in inf)
    for url in urls:
        site = urlopen(url)   
        soup = BeautifulSoup(site, "html.parser")
        eliteTradeIn = soup.find(class_='basicBox').find(class_="bigPrice ats-trade-quote-tradevalue-price").find(class_='priceAmount')   
        tradePrice = eliteTradeIn.text
        eliteTradePrice = tradePrice.replace("*","")
        print(eliteTradePrice)
print("---Retrieved all Elite Trade in Values---")

