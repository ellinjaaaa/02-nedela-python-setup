ir_auto_aplieciba=input("Vai Tev ir autovadītāja apliecība? (jā/nē)").lower()=="jā" 
#.lower() - neatkarīgi no burtu izmēra, programma sapratīs, ka atbilde ir "jā" vai "nē"
ir_students=input("Vai Tu esi students? (jā/nē)").lower()=="jā"   
ir_veterans=input("Vai Tu esi veterāns? (jā/nē)").lower()=="jā"
vecums_teksts=input("Cik Tev gadu?")

try:
    vecums=int(vecums_teksts)
except ValueError:
    print("Lūdzu, ievadi skaitli!")
    exit() #apstādina programmu, citādāk vienkārši turpinātu ar pārējiem jaut. 

if vecums<=0:
    print("Lūdzu, ievadi pozitīvu skaitli!")
    exit() #apstādina programmu, citādāk vienkārši turpinātu ar pārējiem jaut.

#Ievietoju funkciju, kas pārtaisa bool vērtības uz "Jā✓" un "Nē✗
def rezultats(atbilde):
    return "Jā✓" if atbilde else "Nē✗"

#Ievietoju f-strings atbilstoši uzdevuma nosacījumiem - ērtāk, ātrāk un pārskatāmāk.
print(f"Balsošana: {rezultats(vecums >= 18)}")
print(f"Auto īre: {rezultats(vecums >= 21 and ir_auto_aplieciba)}")
print(f"Senioru atlaide: {rezultats(vecums >= 65 or ir_veterans)}")
print(f"Studentu atlaide: {rezultats(16 <= vecums <= 26 and ir_students)}")