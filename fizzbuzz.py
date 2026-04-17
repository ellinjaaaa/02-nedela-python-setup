import sys

if len(sys.argv)<2:
    print("Lūdzu, ievadi skaitli!")
    exit()

try:
    n=int(sys.argv[1])
except ValueError:
    print("Lūdzu, ievadi skaitli!")
    exit()

if n<=0:
    print("Lūdzu, ievadi pozitīvu skaitli!")
    exit()

for a in range(1, n+1): #n+1, tā kā range neiekļautu n, bet gan beigtos ar n-1
    if a%3==0 and a%5==0 and a%7==0:
        print("FizzBuzzJazz", end=" ")
    elif a%3==0 and a%5==0:
        print("FizzBuzz", end=" ")
    elif a%3==0 and a%7==0:
        print("FizzJazz", end=" ")
    elif a%5==0 and a%7==0:
        print("BuzzJazz", end=" ")
    elif a%3==0:
        print("Fizz", end=" ")
    elif a%5==0:
        print("Buzz", end=" ")
    elif a%7==0:
        print("Jazz", end=" ")
    else:
        print(a, end=" ")