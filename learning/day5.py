#highest score of teams
teams=int(input("enter the number of teams:"))
arr=[]
for i in range(0,teams):
    x=int(input("enter the points scored by the team :"))
    arr.append(x)
maxm=0
for score in arr:
    if score>maxm:
        maxm=score

print(maxm)
    
#FizzBuzz
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

#Password Generator
import random
print("Welcome to the pyPassword Generator")
letters=int(input("how many letters would you like in your password?\n"))
symbols=int(input("how many symbols would you like in your password?\n"))
numbers=int(input("how many numbers would you like in your password?\n"))
password=""
range(1,101)
for char in range(1,letters+1):
    password+=random.choice(letters)
