"""
Write down a program to find urls from any website that you
pass as command line argument. You may pass one or multiple
web pages at a time.
"""
import sys, bs4, requests

print('Number of arguments:', len(sys.argv), 'arguments.')
list = sys.argv[1:]
print('Argument List:', list)


def getLinksFromUrl(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        elems = soup.find_all("a")

        for elem in elems:
            print(elem.text)
    except:
        print("Exception occurred when enumerating links in the URL: ",url)
        sys.exc_info()


for url in list:
    getLinksFromUrl(url)

"""
Write a web scraping program to display top 250 movies rated in IMDB.com.Output should be in the specified format
"""
import urllib.request
from bs4 import BeautifulSoup

theurl = "https://www.imdb.com/chart/top"
htmlPage = urllib.request.urlopen(theurl)

#Cooking the Soup
soup = BeautifulSoup(htmlPage,"lxml")
movieList = soup.find_all('tbody', class_="lister-list")

serialNmber =1
for movie in movieList[0].contents:
    if(movie != "\n"):
        movieTitle = movie.find_all('td')[1].text.replace("\n", "")
        print("Ex "+movieTitle.lstrip())
