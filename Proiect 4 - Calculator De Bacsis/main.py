print("Bine ai venit la calculatorul de bacsis!")
total=float(input("Care este factura totala?"))
bacsis=int(input("Cat bacsis ai vrea sa dai? (10, 12 sau 15?) %"))
oameni=int(input("La cati oameni sa se imparta factura? "))

procentaj= 1+ bacsis/100 
per_cap = total / oameni 
final = per_cap * procentaj 
final = format(final, f".2f")
print(f"Fiecare persoana ar trebuii sa plateasca la final:  {final} LEI. ")