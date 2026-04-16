vecums=int(input("Cik Tev gadu?"))
ir_auto_aplieciba=input("Vai Tev ir autovadītāja apliecība? (jā/nē)").lower()=="jā" 
#.lower() - neatkarīgi no burtu izmēra, programma sapratīs, ka atbilde ir "jā" vai "nē"
ir_students=input("Vai Tu esi students? (jā/nē)").lower()=="jā"   
ir_veterans=input("Vai Tu esi veterāns? (jā/nē)").lower()=="jā"

if vecums>=65 or ir_veterans==True:
    print("Tu vari saņemt senioru atlaidi!")
elif vecums>=21 and ir_auto_aplieciba==True:
    print("Tu vari īrēt auto!")
elif 16<=vecums<=26 and ir_students==True:
    print("Tu vari saņemt studentu atlaidi!")
elif vecums>=18:
    print("Tu vari balsot!")
else:
    print("Vēl jāgaida...")
