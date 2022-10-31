print("Bun venit la calculatorul de an bisect!")
an = int(input("Care este anul pe care doriti sa il verificati? "))

if an % 4 == 0:
 if an % 100 == 0:
  if an % 400 == 0:
   print(f"Anul {an} este bisect!")
  else:
   print(f"Anul {an} nu este bisect!") 
 else:
  print(f"Anul {an} este bisect!")
else:
 print(f"Anul {an} nu este bisect!")   
