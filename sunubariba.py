kopa_nauda= int(input())
klientu_sk= int(input())
for i in range(klientu_sk):
min_cena_kg=3000.0
izveletais_zimols=" "
iep_masa= int(input())
iep_cena = input()
kg_cena= iep_cena/iep_masa
if kg_cena<min_cena_kg:


    M, C, brand = input().split()
    M = int(M)
    C = int(C)
    
    if brand != "DOGO":
        cena_kg = C / M
        if cena_kg < min_cena_kg:
            min_cena_kg = cena_kg
            izveletais_zimols = brand
            maisos = K // C

print(f"{izveletais_zimols} {maisos}")