#This program allows us to soup the html page for the xbox one games available to trade.
#We then copy the output to regex101.com to retrive the partial links using regular expressions.
#This also retrieves the title of each game and exports it to a text file.

import re
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup



xboxOneAllGameUrls = "https://www.gamestop.com/trade/browse/_/N-0Z1z13laj?Nrpp=600&Ns=trade.BasePrice%7c1&Ntt=xbox+one"


uClient = uReq(xboxOneAllGameUrls)

page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")

print(page_soup)

saveFile = open('listOfGamesForXboxOne.txt', 'w')
for div in page_soup.find_all('div', class_="title ats-product-quote-title"):
    saveFile.write(div.text + '\n')

saveFile.close()
