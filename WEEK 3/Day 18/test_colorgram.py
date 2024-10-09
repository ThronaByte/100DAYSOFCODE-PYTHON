# import turtle
import colorgram
# from turtle import Turtle, Screen
# import random

color_list = []
colors = colorgram.extract('image.jpg', 35)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_list.append(new_color)

print(color_list)

_=[(243, 242, 239), (171, 158, 33), (99, 6, 51), (75, 94, 173), (232, 209, 73), (10, 35, 127), (178, 104, 155), (215, 89, 34), (105, 123, 210), (26, 96, 40), (33, 103, 47), (242, 237, 240), (113, 131, 212), (184, 116, 161), (218, 92, 40), (232, 235, 244), (235, 241, 235), (207, 168, 79), (120, 21, 54), (137, 63, 91), (3, 29, 122), (169, 183, 228), (132, 175, 140), (220, 174, 190), (95, 148, 106), (230, 178, 160), (169, 206, 175), (12, 81, 26)]
