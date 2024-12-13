import random 

a = True
while a:
 print(random.randint(1,6))
 b= input("Want to roll the dice again?(y/n)")
 if b.lower() == "y":
  continue
 else:
  break
 
