# from turtle import Turtle, Screen
#
# derik = Turtle()
# print(derik)
# derik.shape("turtle")
# derik.color("blue")
# derik.forward(100)
# derik.right(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon", "Type"]
table.align = "l"
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)

print(table)