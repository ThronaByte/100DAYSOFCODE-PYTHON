import pandas
# # challenge 3
data= pandas.read_csv('weather_data.csv')
#
print(data[data.temp == data.temp.max()])