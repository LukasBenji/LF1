zahl = 1
    while zahl != "":
            zahl = input ("Nennen Sie die Zahl: /n")

            if zahl.isdecimal ():
                if int(zahl) % 7 == 0:
                    print(zahl,"ist eine Primzahl")
                else:
                    print(zahl, "Ist keine Primzahl")