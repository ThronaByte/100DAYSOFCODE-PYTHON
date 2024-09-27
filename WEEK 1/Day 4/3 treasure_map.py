# Treasure Map Excercise
row1 = ["♟", "♟", "♟"]
row2 = ["♟", "♟", "♟"]
row3 = ["♟", "♟", "♟"]
map = [row1, row2, row3]
print(f"1 {row1}\n2 {row2}\n3 {row3}")
position = list(input("Where do you want to put the treasure? "))

first = int(position[0])
second = int(position[1])
third = str(first) + str(second)

map[second-1][first - 1] = third

print(f"1 {row1}\n2 {row2}\n3 {row3}")
