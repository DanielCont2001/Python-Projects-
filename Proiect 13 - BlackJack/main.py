from logo_proiect13 import logo 
from turtle import clear
import random

def carte_random():
    carti = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #am pus mai multe valori de 10 pentru cartile Q etc. care au valoarea 10
    carte = random.choice(carti)
    return carte

def calcul_scor(carti):
    
  if sum(carti) == 21 and len(carti) == 2:
        return 0
  if 11 in carti and sum(carti) > 21:
        carti.remove(11)
        carti.append(1)
  return sum(carti)



def compara(scor_utilizator, scor_computer):
    
  if scor_utilizator > 21 and scor_computer > 21:
     return "Ai mers prea mult, ai pierdut 😤"

  if scor_utilizator == scor_computer:
    return "Egalitate 🙃"
  elif scor_computer == 0:
    return "Ai pierdut, calculatorul are Blackjack 😱"
  elif scor_utilizator == 0:
    return "Ai castigat! Blackjack 😎"
  elif scor_utilizator > 21:
    return "Ai mers prea mult, ai pierdut 😭"
  elif scor_computer > 21:
    return "Oponentul a mers prea mult, ai castigat! 😁"
  elif scor_utilizator > scor_computer:
    return "Ai castigat! 😃"
  else:
    return "Ai pierdut! 😤"


def play_games():
  print(logo)

  carti_utilizator = []
  carti_computer = []
  joc_finalizat = False
    

  for i in range(2):
   carti_utilizator.append(carte_random())
   carti_computer.append(carte_random())


  while not joc_finalizat:

    scor_utilizator = calcul_scor(carti_utilizator)
    scor_computer = calcul_scor(carti_computer)
    print(f"        Cartile tale: {carti_utilizator}, scor curent: {scor_utilizator}")
    print(f"        Cartile computerului: {carti_computer[0]}")
    
    if scor_utilizator == 0 or scor_computer == 0 or scor_utilizator > 21:
      joc_finalizat = True 
    else: 

      mesaj = "Apasa 'y' pentru inca o carte si apasa 'n' pentru pass "
      pariaza_user = input(mesaj)
      if pariaza_user == 'y':
        carti_utilizator.append(carte_random())
      else:
        joc_finalizat = True 

  while scor_computer != 0 and scor_computer < 17:
    carti_computer.append(carte_random())
    scor_computer = calcul_scor(carti_computer)
    
  print(f"        Mana ta finala: {carti_utilizator}, scor final: {scor_utilizator}")
  print(f"        Nota finala computer: {carti_computer}, scor final{scor_computer}")
  print(compara(scor_utilizator, scor_computer))



mesaj_start = "Vreti sa jucati BlackJack? Apasa 'y' pentru a incepe sau 'n' pentru a renunta."

while input(mesaj_start) == "y":
  clear()
  play_games()
    

