registernamn = input("registrera användarnamn: ") 
registerlösen = input("registrera lösenord: ") #man registrerar sitt lösenord har och användar namn ovanför

file = open("balance.txt", "r+") #öppnar saldo dokumentet
saldo = float(file.read())
def removeContent():
    file.seek(0)
    file.truncate(0)
    return file
#saldo = float(input("hur mycket pengar har du?: "))

#file.write(str(saldo))

#file.close()


while True: #while loop
    namn = input("användarnamn: ") 
    lösen = input("lösenord: ") #skriver in namn och lösen
    if namn != registernamn: #om namn är inte samma som registernamn går den inte vidare och skriver att det var fel
        print("Fel användarnamn")
        
    elif namn == registernamn: #kollar om det är rätt namn som är skrivet
        print(" ")

        if lösen != registerlösen: #kollar om det är fel lösenord
            print("fel lösenord: ") 
        
        elif lösen == registerlösen:
            print("hej " + namn)
            print("ditt saldo är: " + str(saldo))
            insättning = input("vill du ta ut eller sätta in pengar: ")
            mängd = float(input("Hur mycket? "))
            #file.write
            if insättning == "sätta in":
                saldo = mängd + float(saldo)
                removeContent()
                file.write(str(saldo))
                print("nya saldot är: " + str(saldo))
            elif insättning == "ta ut":
                saldo -= mängd
                print("nya saldot är: " + str(saldo))