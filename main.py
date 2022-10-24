
import pandas

import csv


#
# with open ("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#
#             temperatures.append(int(row[1]))
#
# print(temperatures)
#
#
# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(temp_list)


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels)



data_dict = {
    "Fur Color": ["Gray", "cinnamon", "Black"],
    "Count" : [grey_squirrels, red_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel.scv")