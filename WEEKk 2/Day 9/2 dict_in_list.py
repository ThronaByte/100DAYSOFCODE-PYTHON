travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, visits, cities):
    # my method 1
    log={
            "country": country,
            "visits": visits,
            "cities": cities
    }
    travel_log.append(log)
    # travel_log.insert(-1, log)
    # method 2
    """ log2 = {}
    log2["country"] = country
    log2["visits"] = visits
    log2["cities"] = cities
    # travel_log.append(log2)
    # travel_log.insert(-1, log)
    """
#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



