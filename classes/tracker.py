import geocoder
import os.path
import re
import requests
import json

class Tracker(object):
    def __init__(self):
        try:
            open("tracked_countries", 'x')
        except:
            pass
        self.data = requests.get("https://api.covid19api.com/summary").json()

    def country_search(self, inputCountry):
        for country_ in self.data["Countries"]:
            if country_["Country"].lower() == inputCountry.lower():
                c = country_

        try:
            new_cases = c["NewConfirmed"]
            total_cases = c["TotalConfirmed"]
            total_deaths = c["TotalDeaths"]
        

            print(f"\n{inputCountry.upper()}\n\nNEW CASES: {new_cases}\nTOTAL CASES: {total_cases}\nTOTAL DEATHS: {total_deaths}\n")
        except UnboundLocalError:
            print("Country does not exist")
        


    def tracked_countries(self):
        pass
        

        