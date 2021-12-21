CorrectPassword == "Mastermind"

input("Bitte geben Sie ihr Passwort ein")
if len(passwd) <6:
    print("Es sollte länger sein")
    val = False

if len(passwd) > 20:
    print("Die länge des Passwortes sollte nicht länger als 8 Buchstaben sein.")
    val = False

if not

if not any(char.isdigit() for char in passwd):
    print('Password should have at least one numeral')
    val = False

if not any(char.isupper() for char in passwd):
    print('Password should have at least one uppercase letter')
    val = False

if not any(char.islower() for char in passwd):
    print('Password should have at least one lowercase letter')
    val = False

if not any(char in SpecialSym for char in passwd):
    print('Password should have at least one of the symbols $@#')
    val = False
if val:
    return val


# Main method
def main():
    passwd = 'Geek12@'

    if (password_check(passwd)):
        print("Password is valid")
    else:
        print("Invalid Password !!")