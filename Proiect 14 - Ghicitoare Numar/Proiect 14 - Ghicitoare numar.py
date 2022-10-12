from multiprocessing.resource_sharer import stop
from logo_proiect14 import logo 
from random import randint  
from sys import exit

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """"Verifica ce a ghicit utilizatorul cu raspunsul corect. Returneaza numarul te ture ramase."""
    if guess > answer :
        print("Prea sus.")
        return turns -1
    elif guess < answer:
        print("Prea jos")
        return turns -1
    else:
        print(f"Felicitari! Raspunsul corect a fost: {answer} ")


def set_difficulty():
    """Alege dificultatea. Returneaza numarul de ture pentru dificultatea respectiva"""
    level = input("Ce nivel de greutate ai vrea? Scrie 'easy' sau 'hard': ")
    if level=='easy':
       return EASY_LEVEL_TURNS 
    else:
       return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Bine ati venit la Jocul de ghicire a numarului!")
    print("Eu ma gandesc la un numar de la 1 la 100 (inclusiv)")
    answer = randint(1, 100)

    #print(f"Psst, raspunsul corect este: {answer}") #daca vrei sa verifici numarul!!!

    turns = set_difficulty()

    guess = 0 

    while guess != answer:
       print(f"Mai ai {turns} incercari de a ghici numarul.")
       print(f"\n")

       guess = int(input("Ghiceste numarul: "))

       turns = check_answer(guess, answer, turns)
       if turns == 0:
           print("Ai ramas fara ture de ghicit.. Ai pierdut! :( ")
           quit()
           
           
game()
   


