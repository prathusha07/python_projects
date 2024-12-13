import random
first = float(input("Enter First Number"))
sec = float(input("Enter Second Number"))
opr = str(input("Enter Operators (+,-,*,/ )"))

if opr == '+':
    total = first + sec
elif opr == '-':
    total = first - sec
elif opr == '*':
    total = first * sec
elif opr == '/':
    total = first / sec

else:
    total =str("Please Enter Valid Operator")
 
print(total)

if total == total:
    a= str(input("Do You Want to Continue (Y/N)"))
if a == "Y":
    b = first
else:
    StopIteration

