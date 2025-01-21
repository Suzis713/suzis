print("ievadi kko")
a=int(input())
b=int(input())
c=int(input())
m = True
#pozitivs
if a+b>0 or a+c>0 or b+c>0:
    print("VAR")
else:
    print("NEVAR")
#nulle
if a+b==0 or a+c==0 or b+c==0:
    print("VAR")
else:
    print("NEVAR")
#negativs
if a+b<0 or a+c<0 or b+c<0:
    print("VAR")
else:
    print("NEVAR")