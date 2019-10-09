registernamn = input("registrera användarnamn: ") 
registerlösen = input("registrera lösenord: ") #man registrerar sitt lösenord har och användar namn ovanför

file = open("balance.txt", "r") #öppnar saldo dokumentet
saldo = float(file.read())
file.close()

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
            insättning = input("vill du (ta ut) eller (sätta in) pengar: ")
            
            if insättning == "sätta in":
                mängd = float(input("Hur mycket? "))
                file = open("balance.txt", "w")
                saldo = mängd + float(saldo)
                file.write(str(saldo))
                print("nya saldot är: " + str(saldo))
                file.close()
            elif insättning == "ta ut":
                mängd = float(input("Hur mycket? "))
                file = open("balance.txt", "w")
                saldo -= mängd
                file.write(str(saldo))
                print("nya saldot är: " + str(saldo))
                file.close()
            else:
                print("det finns inget kommando med namnet " + insättning)