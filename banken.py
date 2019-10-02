pin = 1234

userPin = int(input("Skriv in din pinkod: "))

file = open("balance.txt", "w+")
pengar = file.read()
print(pengar)

pengar = input("hur mycket pengar har du?: ")

file.write(pengar)

file.close()

menu = 0
# menu 1 insättning
# menu 2 uttag
# menu 3 avsluta
while menu != 3:
    print("Ditt saldo är: " + pengar)
    menu = int(input("Skriv ditt val[1, 2, 3]: "))
    if menu == 1:
        pengar + str(input("Gör en instättning: "))
    elif menu == 2:
        print("uttag")
    else:
        print("Fel eller avslut")