# challenge 4
import pandas
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241018.csv')
gray_squirrel_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrel_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel_count = len(data[data['Primary Fur Color'] == 'Black'])
# print(len(gray_squirrel_count))
# print(len(red_squirrel_count))
# print(len(black_squirrel_count))

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}
# print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')