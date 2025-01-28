from math import sqrt

Ax=int(input("ievadiet Ax koord sakumpunktu"))
Ay=int(input("ievadiet Ay koord sakumpunktu"))
Bx=int(input("ievadiet Bx koord sakumpunktu"))
By=int(input("ievadiet By koord sakumpunktu"))
Cx=int(input("ievadiet Cx koord sakumpunktu"))
Cy=int(input("ievadiet Cy koord sakumpunktu"))

attalums=sqrt((Ax-Bx)**2+(Ay-By)**2)

if ab>ac and ab>bc:
    garais=ab
    isais1=ac 
    isais2=bc 
elif bc>ab and bc>ac:
    garais=bc 
    isais1=ab 
    isais2=ac 
else:
    garais=ac 
    isais1=ab 
    isais2=bc 

if garais**2==isais1**2+isais2**2:
    print("Veido taisnlenķa trijsturi")
else:
    print("nav")

