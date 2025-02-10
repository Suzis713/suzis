N = int(input())
malka_kopa = int(input())
min_saina_cena = 1000000
for i in range(1, N + 1):
 
saina_masa=int(input())
saina_cena=int(input())
sainu_daudzums =malka_kopa // saina_masa

if malka_kopa % saina_masa > 0:
    sainu_daudzums+=1
nauda = sainu_daudzums * saina_cena
if nauda < min_saina_cena:
    min_saina_cena = nauda

print(min_saina_cena)

