ir_auto_aplieciba=input("Vai Tev ir autovadītāja apliecība? (jā/nē)").lower()=="jā" 
#.lower() - neatkarīgi no burtu izmēra, programma sapratīs, ka atbilde ir "jā" vai "nē"
ir_students=input("Vai Tu esi students? (jā/nē)").lower()=="jā"   
ir_veterans=input("Vai Tu esi veterāns? (jā/nē)").lower()=="jā"
vecums_teksts=input("Cik Tev gadu?")

try:
    vecums=int(vecums_teksts)
except ValueError:
    print("Lūdzu, ievadi skaitli!")
else:
    if vecums<=0:
        print("Lūdzu, ievadi pozitīvu skaitli!")
    else:
        senioru_atlaide=vecums>=65 or ir_veterans==True
        auto_ire=vecums>=21 and ir_auto_aplieciba==True
        studentu_atlaide=16<=vecums<=26 and ir_students==True
        balsojums=vecums>=18
        if senioru_atlaide and auto_ire and studentu_atlaide and balsojums:
            print("Tu vari saņemt senioru atlaidi, studentu atlaidi, īrēt auto un balsot!")
        elif senioru_atlaide and auto_ire and balsojums and not studentu_atlaide:
            print("Tu vari saņemt senioru atlaidi, īrēt auto un balsot, bet ne saņemt student atlaidi!")
        elif senioru_atlaide and studentu_atlaide and balsojums and not auto_ire:
            print("Tu vari saņemt senioru atlaidi, studentu atlaidi un balsot, bet ne īrēt auto!")
        elif auto_ire and studentu_atlaide and balsojums and not senioru_atlaide:
            print("Tu vari īrēt auto, saņemt studentu atlaidi un balsot, bet ne saņemt senioru atlaidi!")
        elif senioru_atlaide and auto_ire and not studentu_atlaide and not balsojums:
            print("Tu vari saņemt senioru atlaidi un īrēt auto, bet ne saņemt studentu atlaidi un ne balsot!")
        elif senioru_atlaide and studentu_atlaide and not auto_ire and not balsojums:
            print("Tu vari saņemt senioru atlaidi un studentu atlaidi!")
        elif senioru_atlaide and balsojums and not auto_ire and not studentu_atlaide:
            print("Tu vari saņemt senioru atlaidi un balsot, bet ne saņemt studentu atlaidi un ne īrēt auto!")
        elif auto_ire and balsojums and not senioru_atlaide and not studentu_atlaide:
            print("Tu vari īrēt auto un balsot, bet ne saņemt senioru atlaidi un ne saņemt studentu atlaidi!")
        elif studentu_atlaide and balsojums and not senioru_atlaide and not auto_ire:
            print("Tu vari saņemt studentu atlaidi un balsot, bet ne saņemt senioru atlaidi un ne īrēt auto!")
        elif senioru_atlaide:
            print("Tu vari tikai saņemt senioru atlaidi!")
        elif auto_ire:
            print("Tu vari tikai īrēt auto!")
        elif studentu_atlaide:
            print("Tu vari saņemt studentu atlaidi!")
        elif balsojums:
            print("Tu vari tikai balsot!")
        else:
            print("Vēl jāgaida...")