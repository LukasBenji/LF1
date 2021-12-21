password = "HalloWelt123"
try = 3

while tries != 0:
    enter = input ("Bitte geben Sie das Passwort ein.")
if  enter == password:
    print("Password korrekt, willkommen.")
    break
else:print("Passwort inkorrekt, bitte erneut eingeben.")
    try =-1
    if try == 0:
        print("Eingabe gesperrt. Sie haben drei Mal das falsche Passwort eingegeben.")