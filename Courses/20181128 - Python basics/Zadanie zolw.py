import turtle
with open('zolw.txt') as komendy:
    for linia in komendy:
        linia = linia.strip() #ta funkcja usuwa wszelkie znaki, które nie są znakami - czyli bałe sacje (usuwa białe znaki z początku  ikońca linii)
        podzielone = linia.split() #przyjmuje argument po ktorym ma podzielic -- domyslny argument spacje
        komenda = podzielone[0]
        kroki = podzielone[1]
        kroki = int(kroki) #konwersja na int jeżeli string wyglada jak liczba
        if komenda == 'B':
            turtle.backward(kroki)
        elif komenda == 'F':
            turtle.forward(kroki)
        elif komenda == 'L':
            turtle.left(kroki)
        elif komenda == 'R':
            turtle.right(kroki)

turtle.mainloop()