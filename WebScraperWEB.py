#This is a webscraper where it gets information for you from any WEBSITE you want

#first pip install beautiful soup
#second pip install requests

#import both of them
from bs4 import BeautifulSoup
import requests

#do any website you want to scrape
#we are doing specific geforce rtx 3000
#make sure you pick a website that lets you use a script a lot of them block you
url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

#this will give us the content of our website
result = requests.get(url)

#this will give us the content in text form in terminal and its basically an html document
#this is just for show make sure you check it then comment it out
#print(result.text)

#what this is for is so we can actually put it in html format and then actually look through the code so it has tags and use html commands
doc = BeautifulSoup(result.text, "html.parser")
print(doc.prettify()) #once you see then you can comment it out again

#now we are trying to find prices of all the cleats
#we will use this so we can access all the dollar signs and that has the prices
prices = doc.find_all(string="$")
#print(prices)#once you check just comment it out

#this is so access the first tag
parent = prices[0].parent
#print(parent)# once you check comment it out

#once we have the parent tag find the strong tag inside the parent tag
strong = parent.find("strong")
#this will print the value inside the strong tag which is the price
print(strong.string)





















