import csv
# Using CSV
with open('weather_data.csv') as weather:
    data = csv.reader(weather)
    temperature = []
    for each_data in data:
        print(each_data)
        if each_data[1] != "temp":
            temperature.append(int(f"{each_data[1]}"))

    print(temperature)