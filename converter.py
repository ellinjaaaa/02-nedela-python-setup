KM_TO_MI=0.621371
MI_TO_KM=1.609344
KG_TO_LB=2.20462
LB_TO_KG=0.45359
L_TO_GAL=0.264172
GAL_TO_L=3.785411
DOL_TO_EUR=0.84235020
EUR_TO_DOL=1.17844087

izvele=input("Ko Tu vēlies konvertēt?(km->mi, mi->km, kg->lb, lb->kg, L->gal, gal->L, $->EUR, EUR->$)") #nebiju pievienojusi mainīgo, 
#tādēļ uzreiz tika izpildīts pats pirmais nosacījums, pat nepievēršoties pārējiem (t.i., automātiski pildīja km->mi)
#visam noņēmu tipu str, tā kā tas nebija nepieciešams, jo jau skaitļiem bija uzlikts float (tā kā pieļaujami decimālskaitļi)
# pievienoju try un except arī gadījumam, ja netiek ievadīti skaitļi - lai programma spētu turpināt darboties 
if izvele=="km->mi":
    try:
        km=float(input("Ievadi attālumu kilometros:"))
        print(f"Attālums jūdzēs ir: {km*KM_TO_MI:.2f}")
    except:
        print("Lūdzu, ievadi derīgu skaitli!")
elif izvele=="mi->km":
    try:
        mi=float(input("Ievadi attālumu jūdzēs:"))
        print(f"Attālums kilometros ir: {mi*MI_TO_KM:.2f}")
    except:
        print("Lūdzu, ievadi derīgu skaitli!")
elif izvele=="kg->lb":
    try:
        kg=float(input("Ievadi masu kilogramos:"))
        print(f"Masa mārciņās ir: {kg*KG_TO_LB:.2f}")
    except:
        print("Lūdzu, ievadi derīgu skaitli!")
elif izvele=="lb->kg":
    try:
        lb=float(input("Ievadi masu mārciņās:"))
        print(f"Masa kilogramos ir: {lb*LB_TO_KG:.2f}")
    except:
        print("Lūdzu, ievadi derīgu skaitli!")
elif izvele=="L->gal":
    try:
        L=float(input("Ievadi tilpumu litros:"))
        print(f"Tilpums galonos ir: {L*L_TO_GAL:.2f}")
    except:
        print("Lūdzu, ievadi derīgu skaitli!")
elif izvele=="gal->L":
    try:
        gal=float(input("Ievadi tilpumu galonos:"))
        print(f"Tilpums litros ir: {gal*GAL_TO_L:.2f}")
    except:
        print("Lūdzu, ievadi derīgu skaitli!")
elif izvele=="$->EUR":
    try:
        DOL=float(input("Ievadi summu dolāros:"))
        print(f"Summa eiro ir: {DOL*DOL_TO_EUR:.2f}")
    except:
        print("Lūdzu, ievadi derīgu skaitli!")
elif izvele=="EUR->$":
    try:
        EUR=float(input("Ievadi summu eiro:"))
        print(f"Summa dolāros ir: {EUR*EUR_TO_DOL:.2f}")
    except:
        print("Lūdzu, ievadi derīgu skaitli!")
else:
    print("Pamēģini vēlreiz!")      