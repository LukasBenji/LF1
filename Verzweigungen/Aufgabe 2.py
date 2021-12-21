bestätigung = "Das ist ein Alkallimetall."
nicht_Bestätigung = "Das ist kein Alkallimetall."
element = input("Ist dieses Element ein Alkalimetall?")
if("Li" == element or "Lithium" == element):
    print(bestätigung)
elif("li" == element or "lithium" == element):
    print(bestätigung)
elif("Na" == element or "Natrium" == element):
    print(bestätigung)
elif("Na" == element or "natrium" == element):
    print(bestätigung)
elif("K" == element or "Kalium" == element):
    print(bestätigung)
elif("K" == element or "kalium" == element):
    print(bestätigung)
elif("Rb" == element or "Rubidium" == element):
    print(bestätigung)
elif("Rb" == element or "rubidium" == element):
    print(bestätigung)
elif("Cs" == element or "Ceasium" == element):
    print(bestätigung)
elif("CS" == element or "ceasium" == element):
    print(bestätigung)
else:
    print(nicht_Bestätigung)



