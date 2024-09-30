def paint_calc(height, width, cover):
    number_of_cans = round((height * width) / cover)
    print(f"You'll need {number_of_cans} cans of paint.")
h = int(input("Height of wall: "))
w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=h, width=w, cover=coverage)