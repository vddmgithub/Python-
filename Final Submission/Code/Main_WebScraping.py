import cv2
from skimage import io
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from Final_Project.Professional import ProfessionalDetails
from Final_Project.TwritterSentiment import TweetListener, SentimentAnalysisWC

#List of professionals interested in.
professionals = []
"""
This is to select the type of analytics that this application offers
    1. Using TextBlob sentiment analysis API
    2. Using Word Count logic   
"""
mechanism = 0

"""
This API achieves URL WebScraping using Beautiful Soap.
This also has the capability to built the final url based on the parameters passes.
"""

def startWebScraping():
    url = "http://m.imdb.com/feature/bornondate"
    parameters = {"sort": 'STARmeter,desc'}
    data = urllib.parse.urlencode(parameters)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    htmlPage = urllib.request.urlopen(req)
    # soup_response = BeautifulSoup(htmlPage, 'lxml')
    soup_response = BeautifulSoup(htmlPage, "html5lib")
    artists = soup_response.find_all("div", class_="lister-item mode-detail", limit=10)

    for artist in artists:
        artist_image = artist.contents[1]
        artist_image_link = artist.contents[1].find("img")["src"]

        artist_details = artist.contents[3]
        artist_Name = artist.contents[3].find("a").text.replace("\n", "")

        details = artist.contents[3].find("p", class_="text-muted text-small").text.split("\n")
        artist_profession = details[1].strip().replace("|", "").rstrip()
        artist_bestWork = details[2].strip()

        profession = ProfessionalDetails(artist_Name, artist_profession, artist_bestWork, artist_image_link)
        professionals.append(profession)

"""
Display Utility that displays image and details of each professional
"""

def displayDetailsOfProfessionals(mechanism):
    index = 1
    for profession in professionals:
        print("Professional: ", index)
        print("Name: ", profession.getName())
        print("Profession: ", profession.getProfession())
        print("Best Work: " + profession.getBestWork())

        if (mechanism == 1):
            print("Overall sentiment on Twitter: ", TweetListener.getSentiment(profession.getName()))
        else:
            print("Overall sentiment on Twitter: ", SentimentAnalysisWC.getSentiment(profession.getName()))

        print("Image source:  ", profession.getImage())
        image = io.imread(profession.getImage())
        cv2.imshow("dst_rt", image)
        cv2.waitKey(5)  # 5 seconds is the time interval between flipping of different images
        print("*" * 151)
        index += 1

"""
Entry point to the Project.
This kicks of URL scraping which inturn kicks of sentimental analysis.
"""

def main():

    print("Started WebScraping of Top 10 professionals: ")
    print(45 * "*")
    startWebScraping()

    # printDetailsOfProfessionals()

    print("Types of twitter Analytics")
    print("1. Twitter API")
    print("2. Word Count")
    mechanism = int(input("Please select the Analytics Mechanism: "))

    professionalsNamesList = []
    for professional in professionals:
        professionalsNamesList.append(professional.getName())

    if (mechanism == 1):
        twitterHandler = TweetListener()
        twitterHandler.authenticate()
        twitterHandler.setCelebrityList(professionalsNamesList)
        twitterHandler.tweetsAnalytics()

    elif (mechanism == 2):
        sentimentAnalysisWC = SentimentAnalysisWC()
        sentimentAnalysisWC.setCelebrityList(professionalsNamesList)
        sentimentAnalysisWC.searchAndAnalyzeTweets()
    else:
        print("Exiting out")
        exit(0)

    displayDetailsOfProfessionals(mechanism)
    exit(0)

main()


