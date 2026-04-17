import random

a=random.randint(1, 100)

print("Tev ir 10 mēģinājumi, lai uzminētu skaitli!")

number_of_guesses=0

while number_of_guesses<10:
    izvele=int(input("Izvēlies skaitli no 1 līdz 100:"))
    number_of_guesses+=1 #palielina mēģinājumu skaitu par 1
    print(f"Šis bija Tavs {number_of_guesses}. mēģinājums.")
    if izvele>a:
        print("Tevis izvēlētais skaitlis ir par lielu!")
    elif izvele<a:
        print("Tevis izvēlētais skaitlis ir par mazu!")
    else:
        print("Apsveicu! Tu uzminēji skaitli!")
        break

print(f"Pareizas skaitlis: {a}")
exit()