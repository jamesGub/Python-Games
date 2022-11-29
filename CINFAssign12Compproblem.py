#CINF 308 - Assignment 12: Company Solution
#This is James Gillanders' code

#For this program, we will be echoing what I went over in my discussion post, being the implementation of a weather forecast for a meteorology company or organization.
#While this is not a direct "problem", it can definitely excel the company's capabilities at tracking weather and could be interactive on the user side as well. 

#This is the first step for this program, using the requests library allows us to
#extract data from HTTP requests, these include the "Get" request and more but we will be using "get".
import requests
 
print("This is the weather API, please enter a city you would like to see the forecast of!")
la_ville = input("Enter the city you'd like to see the weather data for: ")
#Sample text to fetch the input of the city the user enters.
 
#Next we have to create a fucntion that will extract the data from the HTTP.
#Where is this data coming from? It will be wttr.in, a weather service that 
#returns accurate data in the form of infographics. 

#one parameter needed, also try/except to check for any errors.
def extraction(take):
    source_data = 'https://wttr.in/{}'.format(take)
    try:
        forecast = requests.get(source_data)
        retrieval = forecast.text
    except:
        retrieval = "Error Occurred"
    print(retrieval)
     
extraction(la_ville)