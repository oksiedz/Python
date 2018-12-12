import turtle
zmienna = True
turtle.forward(10)
if zmienna: #czy jest prawda
    turtle.right(90)
else:
    turtle.left(90)
turtle.forward(30)
dystans = 0
while dystans < 50:
    turtle.forward(10)
    dystans = dystans + 10
for liczba in range(4):
    turtle.forward(10)
    turtle.left(90)
turtle.forward(10)
def kwadrat(dlugosc_boku):
    for i in range(4):
        turtle.forward(dlugosc_boku)
        turtle.left(90)
kwadrat(10)
kwadrat(20)
kwadrat(50)
turtle.forward(10)
turtle.right(100)
turtle.forward(10)
turtle.left(100)
turtle.forward(10)
turtle.mainloop()