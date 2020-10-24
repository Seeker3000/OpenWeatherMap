# Copyright (c) 2020 D.Damian
# Released under the MIT license
# ************************************************************************************************
# Developed with Python 3.8.2
# Tested in IDLE
# You need to insert the private Open Weather Map API key in the variable   appid_private
# ************************************************************************************************
import requests, json, datetime, pprint, urllib

with open("city.list.json", "r") as rf:
    weather_data = json.load(rf)

to_find = input("Enter the name of the city: ")

for s in range(len(weather_data)):
        if weather_data[s]["name"] == to_find:
            print("The location of {} is {}.".format(weather_data[s]["name"], weather_data[s]["coord"]))
            var = weather_data[s]["coord"]


lat_coord = var['lat']
lon_coord = var['lon']

print("I will call the Open Weather API for: \n" + to_find + " with:" + " latitude: " + str(lat_coord) + " and longitude:" + str(lon_coord))

#you need to add your private Open Weather Map API key here
appid_private = "your key"
#-----------------------------------------------

args = {"lat": lat_coord, "lon": lon_coord, "exclude": "minutely,hourly", "units": "metric", "appid": appid_private}
url = "https://api.openweathermap.org/data/2.5/onecall?{}".format(urllib.parse.urlencode(args))
res = requests.get(url)
data = res.json()

A = data["current"]
timp= datetime.datetime.fromtimestamp(int(A["dt"])).strftime('%W \ %A \ %d:%-m:%Y')
rasarit= datetime.datetime.fromtimestamp(int(A["sunrise"])).strftime('%H:%M:%S')
apus= datetime.datetime.fromtimestamp(int(A["sunset"])).strftime('%H:%M:%S')
now_temp = A["temp"]
now_pressure = A["pressure"]
now_humid = A["humidity"]
now_uvi = A["uvi"]
now_condition_icon = A["weather"][0]['icon']
now_condition_description = A["weather"][0]['description']

B = data['daily']
timp0= datetime.datetime.fromtimestamp(int(B[0]["dt"])).strftime('%W \ %A \ %d:%-m:%Y')
rasarit0= datetime.datetime.fromtimestamp(int(B[0]["sunrise"])).strftime('%H:%M:%S')
apus0= datetime.datetime.fromtimestamp(int(B[0]["sunset"])).strftime('%H:%M:%S')
now_temp_min_0 = B[0]["temp"]['min']
now_temp_max_0 = B[0]["temp"]['max']
now_pressure0 = B[0]["pressure"]
now_humid0 = B[0]["humidity"]
now_uvi0 = B[0]["uvi"]
now_condition_icon0 = B[0]["weather"][0]['icon']
now_condition_description0 = B[0]["weather"][0]['description']

timp1= datetime.datetime.fromtimestamp(int(B[1]["dt"])).strftime('%W \ %A \ %d:%-m:%Y')
rasarit1= datetime.datetime.fromtimestamp(int(B[1]["sunrise"])).strftime('%H:%M:%S')
apus1= datetime.datetime.fromtimestamp(int(B[1]["sunset"])).strftime('%H:%M:%S')
now_temp_min_1 = B[1]["temp"]['min']
now_temp_max_1 = B[1]["temp"]['max']
now_pressure1 = B[1]["pressure"]
now_humid1 = B[1]["humidity"]
now_uvi1 = B[1]["uvi"]
now_condition_icon1 = B[1]["weather"][0]['icon']
now_condition_description1 = B[1]["weather"][0]['description']

timp2= datetime.datetime.fromtimestamp(int(B[2]["dt"])).strftime('%W \ %A \ %d:%-m:%Y')
rasarit2= datetime.datetime.fromtimestamp(int(B[2]["sunrise"])).strftime('%H:%M:%S')
apus2= datetime.datetime.fromtimestamp(int(B[2]["sunset"])).strftime('%H:%M:%S')
now_temp_min_2 = B[2]["temp"]['min']
now_temp_max_2 = B[2]["temp"]['max']
now_pressure2 = B[2]["pressure"]
now_humid2 = B[2]["humidity"]
now_uvi2 = B[2]["uvi"]
now_condition_icon2 = B[2]["weather"][0]['icon']
now_condition_description2 = B[2]["weather"][0]['description']

timp3= datetime.datetime.fromtimestamp(int(B[3]["dt"])).strftime('%W \ %A \ %d:%-m:%Y')
rasarit3= datetime.datetime.fromtimestamp(int(B[3]["sunrise"])).strftime('%H:%M:%S')
apus3= datetime.datetime.fromtimestamp(int(B[3]["sunset"])).strftime('%H:%M:%S')
now_temp_min_3 = B[3]["temp"]['min']
now_temp_max_3 = B[3]["temp"]['max']
now_pressure3 = B[3]["pressure"]
now_humid3 = B[3]["humidity"]
now_uvi3 = B[3]["uvi"]
now_condition_icon3 = B[3]["weather"][0]['icon']
now_condition_description3 = B[3]["weather"][0]['description']

timp4= datetime.datetime.fromtimestamp(int(B[4]["dt"])).strftime('%W \ %A \ %d:%-m:%Y')
rasarit4= datetime.datetime.fromtimestamp(int(B[4]["sunrise"])).strftime('%H:%M:%S')
apus4= datetime.datetime.fromtimestamp(int(B[4]["sunset"])).strftime('%H:%M:%S')
now_temp_min_4 = B[4]["temp"]['min']
now_temp_max_4 = B[4]["temp"]['max']
now_pressure4 = B[4]["pressure"]
now_humid4 = B[4]["humidity"]
now_uvi4 = B[4]["uvi"]
now_condition_icon4 = B[4]["weather"][0]['icon']
now_condition_description4 = B[4]["weather"][0]['description']

timp5= datetime.datetime.fromtimestamp(int(B[5]["dt"])).strftime('%W \ %A \ %d:%-m:%Y')
rasarit5= datetime.datetime.fromtimestamp(int(B[5]["sunrise"])).strftime('%H:%M:%S')
apus5= datetime.datetime.fromtimestamp(int(B[5]["sunset"])).strftime('%H:%M:%S')
now_temp_min_5 = B[5]["temp"]['min']
now_temp_max_5 = B[5]["temp"]['max']
now_pressure5 = B[5]["pressure"]
now_humid5 = B[5]["humidity"]
now_uvi5 = B[5]["uvi"]
now_condition_icon5 = B[5]["weather"][0]['icon']
now_condition_description5 = B[5]["weather"][0]['description']

timp6= datetime.datetime.fromtimestamp(int(B[6]["dt"])).strftime('%W \ %A \ %d:%-m:%Y')
rasarit6= datetime.datetime.fromtimestamp(int(B[6]["sunrise"])).strftime('%H:%M:%S')
apus6= datetime.datetime.fromtimestamp(int(B[6]["sunset"])).strftime('%H:%M:%S')
now_temp_min_6 = B[6]["temp"]['min']
now_temp_max_6 = B[6]["temp"]['max']
now_pressure6 = B[6]["pressure"]
now_humid6 = B[6]["humidity"]
now_uvi6 = B[6]["uvi"]
now_condition_icon6 = B[6]["weather"][0]['icon']
now_condition_description6 = B[6]["weather"][0]['description']

timp7= datetime.datetime.fromtimestamp(int(B[7]["dt"])).strftime('%W \ %A \ %d:%-m:%Y')
rasarit7= datetime.datetime.fromtimestamp(int(B[7]["sunrise"])).strftime('%H:%M:%S')
apus7= datetime.datetime.fromtimestamp(int(B[7]["sunset"])).strftime('%H:%M:%S')
now_temp_min_7 = B[7]["temp"]['min']
now_temp_max_7 = B[7]["temp"]['max']
now_pressure7 = B[7]["pressure"]
now_humid7 = B[7]["humidity"]
now_uvi7 = B[7]["uvi"]
now_condition_icon7 = B[7]["weather"][0]['icon']
now_condition_description7 = B[7]["weather"][0]['description']


var = to_find + " on the date CW:" + str(timp)+" has the following weather:"+ "\n Sunrise = "+str(rasarit)+"\n Sunset = "+str(apus)+"\n (°C) = "+str(now_temp)+"\n Pressure = "+str(now_pressure)+"\n Humidity (%) = "+str(now_humid)+"\n UV Index = "+str(now_uvi)+"\n State = "+str(now_condition_description)
var0 = to_find + " on the date CW:" + str(timp0)+" has the following weather:"+ "\n Sunrise = "+str(rasarit0)+"\n Sunset = "+str(apus0)+"\n Min (°C) = "+str(now_temp_min_0)+ "\n Max (°C) = "+str(now_temp_max_0)+"\n Pressure = "+str(now_pressure0)+"\n Humidity (%) = "+str(now_humid0)+"\n UV Index = "+str(now_uvi0)+"\n State = "+str(now_condition_description0)
var1 = to_find + " on the date CW:" + str(timp1)+" has the following weather:"+ "\n Sunrise = "+str(rasarit1)+"\n Sunset = "+str(apus1)+"\n Min (°C) = "+str(now_temp_min_1)+ "\n Max (°C) = "+str(now_temp_max_1)+"\n Pressure = "+str(now_pressure1)+"\n Humidity (%) = "+str(now_humid1)+"\n UV Index = "+str(now_uvi1)+"\n State = "+str(now_condition_description1)
var2 = to_find + " on the date CW:" + str(timp2)+" has the following weather:"+ "\n Sunrise = "+str(rasarit2)+"\n Sunset = "+str(apus2)+"\n Min (°C) = "+str(now_temp_min_2)+ "\n Max (°C) = "+str(now_temp_max_2)+"\n Pressure = "+str(now_pressure2)+"\n Humidity (%) = "+str(now_humid2)+"\n UV Index = "+str(now_uvi2)+"\n State = "+str(now_condition_description2)
var3 = to_find + " on the date CW:" + str(timp3)+" has the following weather:"+ "\n Sunrise = "+str(rasarit3)+"\n Sunset = "+str(apus3)+"\n Min (°C) = "+str(now_temp_min_3)+ "\n Max (°C) = "+str(now_temp_max_3)+"\n Pressure = "+str(now_pressure3)+"\n Humidity (%) = "+str(now_humid3)+"\n UV Index = "+str(now_uvi3)+"\n State = "+str(now_condition_description3)
var4 = to_find + " on the date CW:" + str(timp4)+" has the following weather:"+ "\n Sunrise = "+str(rasarit4)+"\n Sunset = "+str(apus4)+"\n Min (°C) = "+str(now_temp_min_4)+ "\n Max (°C) = "+str(now_temp_max_4)+"\n Pressure = "+str(now_pressure4)+"\n Humidity (%) = "+str(now_humid4)+"\n UV Index = "+str(now_uvi4)+"\n State = "+str(now_condition_description4)
var5 = to_find + " on the date CW:" + str(timp5)+" has the following weather:"+ "\n Sunrise = "+str(rasarit5)+"\n Sunset = "+str(apus5)+"\n Min (°C) = "+str(now_temp_min_5)+ "\n Max (°C) = "+str(now_temp_max_5)+"\n Pressure = "+str(now_pressure5)+"\n Humidity (%) = "+str(now_humid5)+"\n UV Index = "+str(now_uvi5)+"\n State = "+str(now_condition_description5)
var6 = to_find + " on the date CW:" + str(timp6)+" has the following weather:"+ "\n Sunrise = "+str(rasarit6)+"\n Sunset = "+str(apus6)+"\n Min (°C) = "+str(now_temp_min_6)+ "\n Max (°C) = "+str(now_temp_max_6)+"\n Pressure = "+str(now_pressure6)+"\n Humidity (%) = "+str(now_humid6)+"\n UV Index = "+str(now_uvi6)+"\n State = "+str(now_condition_description6)
var7 = to_find + " on the date CW:" + str(timp7)+" has the following weather:"+ "\n Sunrise = "+str(rasarit7)+"\n Sunset = "+str(apus7)+"\n Min (°C) = "+str(now_temp_min_7)+ "\n Max (°C) = "+str(now_temp_max_7)+"\n Pressure = "+str(now_pressure7)+"\n Humidity (%) = "+str(now_humid7)+"\n UV Index = "+str(now_uvi7)+"\n State = "+str(now_condition_description7)

print(var)
print(var1)
print(var2)
print(var3)
print(var4)
print(var5)
print(var6)
print(var7)
