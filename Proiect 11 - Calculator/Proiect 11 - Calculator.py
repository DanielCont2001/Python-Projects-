from logo_proiect11 import logo

# Adunare
def add(n1,n2):
  return n1+n2
#Scadere
def substract(n1,n2):
  return n1-n2
#Inmultire
def multiply(n1,n2):
  return n1*n2
#Impartire
def divide(n1,n2):
  return n1/n2

operations={
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  num1= float(input('Dati primul numar = '))
  for symbol in operations:
    print(symbol)
  should_continue=True
  
  while should_continue:
    operation_symbol= input('Alege un operator (semn) pentru a efectua calculul: ')
    num2= float(input('Dati urmatorul numar = '))
    calculation_function= operations[operation_symbol]
    answer= calculation_function(num1,num2)
  
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Scrie 'y' pentru a continua cu {answer} sau 'n' pentru a porni un alt calcul: ") == "y":
      num1=answer
    else:
      should_continue=False
      calculator()
    
calculator()