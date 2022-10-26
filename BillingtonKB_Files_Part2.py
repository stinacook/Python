# Chapter 10: Files Part 2
# Name: Kristina Billington
# Date: 24 OCT 2022

import json

#Read file for list from file_manage.txt.
imported_data = 'file_mileage.txt'

with open(imported_data) as file_object:
    contents = json.load(file_object)

#create header for the printed table.
print('=' * 75)
print(f'Date    \tTrip \tGallons\tCost  \t$/G    \tMileage')
print('*' * 75)

#iterate through list for stored dictionary items.
for i in contents:
   #assign variables for key values so they can be divided to find $/G and Mileage.
   #convert data type from string to float.
   float_cost = float(i['cost'])
   float_gallons = float(i['gallons'])
   float_trip = float(i['trip'])

   #perform math functions. Round to 2 decimal places.
   price_gallon= round((float_cost / float_gallons),2)
   mileage2 = round((float_trip / float_gallons),2)

   #print the table to display trip information.
   print(f" {i['date']}\t{i['trip']}\t{i['gallons']}\t${i['cost']}\t${price_gallon} \t{mileage2}")

print('=' * 75) 





