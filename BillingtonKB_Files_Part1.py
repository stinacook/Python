# Chapter 10: Files Part 1
# Name: Kristina Billington
# Date: 24 OCT 2022


#Create dictionaries for file_mileage.txt

import json 

filename = "file_mileage.txt"
all_trips = []

mileage1 = {
    "date": "5/2/2008",
    "trip": "293.7",
    "gallons":"17.931",
    "cost":"62.02"
    }

mileage2 = {
    "date": "5/8/2008",
    "trip":"314",
    "gallons":"17.044",
    "cost":"59.47",
    }

mileage3 = {
    "date": "5/14/2008",
    "trip":"316",
    "gallons":"17.256",
    "cost":"63.66",
    }

mileage4 = {
    "date":"5/19/2008",
    "trip":"288.3",
    "gallons":"16.058",
    "cost":"58.60",
    }

mileage5 = {
    "date":"5/23/2008",
    "trip":"223.8",
    "gallons":"12.015",
    "cost":"46.85"
    }

#append all of the dictionaries into a list called all_trips:

all_trips.append(mileage1)
all_trips.append(mileage2)
all_trips.append(mileage3)
all_trips.append(mileage4)
all_trips.append(mileage5)

#write all_trips list to file_mileage.txt as a json string:

with open(filename, "w") as data:
    data.write(json.dumps(all_trips))


#print(all_trips)
