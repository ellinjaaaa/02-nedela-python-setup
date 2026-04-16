#1.uzd.
#Piešķirt vismaz 2 pamata tipu vērtības mainīgajiem (str, int, float, bool, None)
print(float(6.28076497327))
print(int(1010101001))

#Konsoles izvade ar katras vērtības tipu, izmantojot type()
vards="Līga"
vecums=34
print("Vārda tips ir", type(vards))
print("Vecuma tips ir", type(vecums))

#Vismaz 3 Python truthy/falsy uzvedības piemērus ar komentāriem
print(bool([2,4,6,8]))       #True! (saraksts - kaut kas ir)
print(bool(67))              #True! (skaitlis - kaut kas ir)
print(bool(0.0))             #False! (nulle - tukšums jeb nekā nav)
print(bool(None))            #False! (None - tukšums jeb nekā nav)

#Vismaz 3 tiešās datu tipu pārveides (explicit conversion) ar robežgadījumiem (kas notiek, ja konversija neizdodas)
augums="1.756"
print(float(augums))         #No str uz float
print(int(float(augums)))    #Divsoļu pārveidošana no str uz float un tad uz int

word="ābc"
#print(int("ābc")) -> ValueError: 1.noskaidrot tipu; 2.uzrakstīt print komandu ar pareizo tipu
print(type(word))       #Noskaidroju, ka <class 'str'>
print(str(word))

augums_teksts=input("Kāds ir tavs augums?")
augums=float(augums_teksts)
print(f"Ja Tu uzvilktu augstpapēžu kurpes, tad Tavs augums būtu {augums+0.08} metri!")

#print(int("3.14")) # ValueError! No sākuma jākonvertē uz float, un tikai tad uz int, jo "3.14" ir str

print(float("1e4")) #10000.0

# Virkņu savienošana — Python neveic automātisku tipu konversiju
print("7"+"3") #virkņu savienošana
print(int("7")+int("3")) #skaitļu saskaitīšana pēc konversijas no str uz int abiem skaitļiem
print(int("7")+3) #skaitļu saskaitīšana pēc konversijas no str uz int vienam no sk.

#Aritmētika
print(10+3) #Saskaitīšana
print(10-3) #Atņemšana
print(10*3) #Reizināšana
print(10/3) #Dalīšana (vienmēr float rezultāts)
print(10//3) #Veselo skaitļu dalīšana
print(10%3) #Atlikums pēc dalīšanas
print(10**3) #Kāpināšana
print(10-True) #True=1
print(10*False) #False=0
print(10/True) #True=1
#print(10/False) #False=0; ZeroDivisionError: nedrīkst dalīt ar nulli

#Citi interesanti gadījumi, izskaidrot kāpēc tā notiek.
print(0.1 + 0.2 == 0.3) # False, kāpēc - decimālskaitļi binārajā sistēmā nav precīzi - nepieciešama noapaļošana
print(round(0.1+0.2,1)==0.3) #True, noapaļojot līdz vienam ciparam aiz komata, iegūst 0.3
print(round(0.1+0.2,2)==0.3) #True, noapaļojot līdz diviem cipariem aiz komata, iegūst 0.3
print(round(2.5)) # 2 - banker's rounding: ja skaitlis ir pa vidu, tas tiek noapaļots uz tuvāko pāra skaitli
print(round(3.5)) # 4 - banker's rounding: ja skaitlis ir pa vidu, tas tiek noapaļots uz tuvāko pāra skaitli