#! /usr/bin/python3

"""
Basic weather app for CLI
Date: Tue Sep 11 23:55:59 EDT 2018

To get Yahoo weather data
$ pip3 install weather-api

For color output
$ pip3 install colorama

WOEID for Lexington, KY is 12775316
"""

from weather import Weather, Unit
from colorama import Fore, Style
import os

# To clear the screen
cls = os.system('clear')

weather = Weather(unit=Unit.FAHRENHEIT)
lookup = weather.lookup(12775316)
condition = lookup.condition
place = lookup.title
forecasts = lookup.forecast

print(Style.BRIGHT)
print("\n" + "Weather for " + place + "\n")
print("Today's date: " + "\t\t\t" + condition.date)
print("Current conditions: " + "\t\t" + condition.text)
print("Current temperature: " + "\t\t" + condition.temp + "F")
print("\n" + "Forecast for Lexington, KY:" + "\n")

for forecast in forecasts:
    print(Fore.MAGENTA + forecast.date + "\t" + 
            Fore.WHITE + "High temp: " + forecast.high + "F" + "\t" +
            "Low temp: " + forecast.low + "F" + "\t" +
            Fore.RED + forecast.text + "\n")
