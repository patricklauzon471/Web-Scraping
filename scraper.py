# The request module allows you to send HTTP Requests using Python
#The HTTP request eturns a response object with response data
#Request.get sends a get request to the url
import requests
#This module allows for the capwords function to be used
#This function splits the strings into words using .split
import string
#Beautiful Soup is a Python library that makes it easy
#To scrape information from web pages
#Beautiful soup parses HTML documents
from bs4 import BeautifulSoup

#Prompts the user to enter a search
Enter_input = input("Search: ")
#Breaks the entry into seperate words and capitilizations
u_i = string.capwords(Enter_input)
#Splits the seperate words into a list seperated by a coma
lists = u_i.split()
#Joining with a delimiter brings all the words together
#But seperates them with an underscore
word = "_".join(lists)

#The URL becomes the wkipedia homepage + the entered word
url = "https://en.wikipedia.org/wiki/" + word

def wikibot(url):
    #Get request to the url
    url_open = requests.get(url)
    #.content gets all the child elements and text nodes as a list
    #BeatifulSoup has 2 parts, the HTML doc and parser
    #This builds the oup object from HTML text
    soup = BeautifulSoup(url_open.content, 'html.parser')
    #HTML table consists of columns and rows
    #Wkipedia infobox is a fixed format table added to
    #top right corner. This means we'll be getting info
    #Directly from the infobox (found using isnpect on wiki page)
    details = soup('table', {'class':'infobox'})
    for i in details:
        #The find_all method is used to find all tags with
        #The specified tag name, the tr element defines a row
        #Of cells in a table
        h = i.find_all('tr')
        for j in h:
            #find_all method for the header label and
            #the data cells 
            heading = j.find_all('th')
            detail = j.find_all('td')
            #If heading and detail both contain information
            #Need to display it
            if heading is not None and detail is not None:
#The zip function has the first item of each list paired together
#and so on so the first item in heading and detail will be paired
                for x,y in zip(heading, detail):
                    print("{} :: {}".format(x.text, y.text))
                    print("-----------------------")
    for i in range(1, 3):
        print(soup('p')[i].text)
wikibot(url)


