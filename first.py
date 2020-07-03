from selenium import webdriver
from beautifulsoup4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

products = []
prices = []
ratings = []
driver.get("https://www.flipkart.com/gaming-laptops-store?otracker=nmenu_sub_Electronics_0_Gaming%20Laptops&otracker=nmenu_sub_Electronics_0_Gaming%20Laptops")

content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll('a',href=True,attrs={'class':'_2cLu-l'}):
    name=a.find('div',attrs={'class':'_2cLu-l'})
    price = a.find('div',attrs={'class':'_1vC4OE'})
    ratings = a.find('div',attrs={'class':'hGSR34'})
    products.append(name.text)
    price.append(price.text)
    ratings.append(rating.text)
