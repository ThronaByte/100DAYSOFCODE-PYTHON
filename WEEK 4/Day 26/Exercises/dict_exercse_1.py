sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
result = {sent:len(sent) for sent in sentence.split()}


# print(result)


for word, length in result.items():
    print(f"{word}: {length}")
