#Password Generator Project
import random
from xml.dom.minidom import CharacterData

litere = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numere = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simboluri = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bine ati venit : Generatorul PyPassword")
nr_litere = int(input("Cate litere ai vrea sa contina parola ta?\n"))
nr_simboluri = int(input(f"Cate simboluri ai vrea sa contina parola ta??\n"))
nr_numere = int(input(f"Cate cifre ai vrea sa contina parola ta?\n"))

parola = ""
for litera in range(1, nr_litere+1):
  caracter = random.choice(litere)
  parola = parola + caracter 

for simbol in range(1, nr_simboluri+1):
  caracter = random.choice(simboluri)
  parola = parola + caracter 
 
for cifra in range(1, nr_numere+1):
  caracter = random.choice(numere)
  parola = parola + caracter  
 
print("Parola ta este: " + parola) #sau print(f"Parola ta este: {parola})

