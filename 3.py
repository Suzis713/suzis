from math import sqrt

Ax=int(input("ievadiet Ax koord sakumpunktu"))
Ay=int(input("ievadiet Ay koord sakumpunktu"))
Bx=int(input("ievadiet Bx koord sakumpunktu"))
By=int(input("ievadiet By koord sakumpunktu"))
Cx=int(input("ievadiet Cx koord sakumpunktu"))
Cy=int(input("ievadiet Cy koord sakumpunktu"))

attalums=sqrt((Ax-Bx)**2+(Ay-By)**2)
print(attalums)

