KM_TO_MI=0.621371
MI_TO_KM=1.609344
KG_TO_LB=2.20462
LB_TO_KG=0.45359
L_TO_GAL=0.264172
GAL_TO_L=3.785411
DOL_TO_EUR=0.84235020
EUR_TO_DOL=1.17844087

input("Ko Tu vēlies konvertēt?(km->mi, mi->km, kg->lb, lb->kg, L->gal, gal->L, $->EUR, EUR->$)")
if input==str("km->mi"):
    km=float(str(input("Ievadi attālumu kilometros:")))
    print(f"Attālums jūdzēs ir: {km*KM_TO_MI:.2f}")
elif input==str("mi->km"):
    mi=float(str(input("Ievadi attālumu jūdzēs:")))
    print(f"Attālums kilometros ir: {mi*MI_TO_KM:.2f}")
elif input==str("kg->lb"):
    kg=float(str(input("Ievadi masu kilogramos:")))
    print(f"Masa mārciņās ir: {kg*KG_TO_LB:.2f}")
elif input==str("lb->kg"):
    lb=float(str(input("Ievadi masu mārciņās:")))
    print(f"Masa kilogramos ir: {lb*LB_TO_KG:.2f}")
elif input==str("L->gal"):
    L=float(str(input("Ievadi tilpumu litros:")))
    print(f"Tilpums galonos ir: {L*L_TO_GAL:.2f}")
elif input==str("gal->L"):
    gal=float(str(input("Ievadi tilpumu galonos:")))
    print(f"Tilpums litros ir: {gal*GAL_TO_L:.2f}")
elif input==str("$->EUR"):
    DOL=float(str(input("Ievadi summu dolāros:")))
    print(f"Summa eiro ir: {DOL*DOL_TO_EUR:.2f}")
elif input==str("EUR->$"):
    EUR=float(str(input("Ievadi summu eiro:")))
    print(f"Summa dolāros ir: {EUR*EUR_TO_DOL:.2f}")
else:
    print("Pamēģini vēlreiz!")      