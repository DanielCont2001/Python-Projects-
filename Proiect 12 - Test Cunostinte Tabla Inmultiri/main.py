import random
#elemente de prezentare

a22 = 6*8
print(a22)

print('-----------------------------------')
print('Tabla inmultirii - test de evaluare')
print('-----------------------------------')
print('Efectuati corect cele 10 operatii!')
print('-----------------------------------')
print('Apasa o tasta pentru a incepe...')
input()
#incepem testul...
ok = 1
for x in range(10):
    print("Operatia",x+1,"din 10:")
    n = random.randint(1,10)
    m = random.randint(1,10)
    rez = n * m
    rasp = int(input(str(n)+" * "+str(m)+" = "))
    if rasp == rez:
        print('Corect!')
        ok = ok + 0.9
    else:
        print('Incorect!',str(n)+" * "+str(m)+" =", n*m)
    print('------------')
#la final, evaluez rezultatele
if ok<5:
    print('Ai obtinut', round(ok),'! Mai invata...')
elif ok<8:
    print('Ai obtinut', round(ok),'! Atentie...')
elif ok<10:
    print('Ai obtinut', round(ok),'! Aproape perfect...')
else:
    print('Zece! Felicitari!')