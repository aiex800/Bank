registernamn = input("registrera användarnamn: ") 
registerlösen = input("registrera lösenord: ") #man registrerar sitt lösenord och användar namn ovanför

file = open("balance.txt", "r") #öppnar saldo dokumentet
saldo = float(file.read()) #saldo blir file som float och det läser bara
file.close() #stänger filen

while True: #while loop
    namn = input("användarnamn: ") 
    lösen = input("lösenord: ") #skriver in namn och lösen
    if namn != registernamn: #om namn är inte samma som registernamn går den inte vidare och skriver att det var fel
        print("Fel användarnamn")
        
    elif namn == registernamn: #kollar om det är rätt namn som är skrivet
        print(" ")

        if lösen != registerlösen: #kollar om det är fel lösenord
            print("fel lösenord: ") 
        
        elif lösen == registerlösen: #kollar om det är rätt lösenord
            print("hej " + namn)
            print("ditt saldo är: " + str(saldo))
            insättning = input("vill du (ta ut) eller (sätta in) pengar: ") #frågar om man vill sätta in eller ta ut pengar
            
            if insättning == "sätta in": #om man skrivit sätta in kör den detta
                mängd = float(input("Hur mycket? ")) 
                file = open("balance.txt", "w") #öppnar balance.txt som write
                saldo = mängd + float(saldo) #plusar ihop pengarna
                file.write(str(saldo)) #skriver över allt som är i filen till det saldo är
                print("nya saldot är: " + str(saldo))
                file.close() #stänger filen
            elif insättning == "ta ut":
                mängd = float(input("Hur mycket? "))
                file = open("balance.txt", "w") #öppnar i write
                saldo -= mängd 
                file.write(str(saldo)) #subtraherar pengarna
                print("nya saldot är: " + str(saldo))
                file.close() # stänger filen
            else:
                print("det finns inget kommando med namnet " + insättning) #om man skriver ett alternativ som inte finns skrivs detta
