print("Bun venit la calculatorul de indice de masa corporala (IMC)")

height = input("Inaltimea (metri) : ")
weight = input("Greutatea (kg) : ")

inaltime=float(height) 
greutate=float(weight) 

imc= greutate / (inaltime*inaltime)
imc_nou = int(imc)

print("IMC-ul dvs. este: " + str(imc_nou))

#print("Valorile IMC se raporteaza astfel: ")
#print("Valorile IMC se raporteaza astfel: ")
#print("intre 18,50 si 24,99 - Greutate normala")
#print("intre 25,00 si 29,99 - Supraponderal")
#print("intre 30,00 si 34,99 - Obezitate (gradul I)")
#print("intre 35,00 si 39,99 - Obezitate (gradul II)")
#print("40,00 sau mai mult - Obezitate morbidă")
