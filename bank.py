registernamn = input("registrera användarnamn: ")
registerlösen = input("registrera lösenord: ")

file = open("balance.txt", "w+")
saldo = file.read()
print(saldo)

saldo = float(input("hur mycket pengar har du?: "))

file.write(str(saldo))

file.close()


while True:
    namn = input("användarnamn: ")
    lösen = input("lösenord: ")
    if namn != registernamn:
        print("Fel användarnamn")
        
    elif namn == registernamn:
        print(" ")

    if lösen != registerlösen:
        print("fel lösenord: ")

    elif lösen != registerlösen + namn != registernamn :
        print("hej " + namn)
        print("ditt saldo är: " + str(saldo))
        insättning = input("vill du ta ut eller sätta in pengar: ")
        mängd = float(input("Hur mycket? "))
        if insättning == "sätta in":
            saldo += mängd
            print("nya saldot är: " + str(saldo))
        elif insättning == "ta ut":
            saldo -= mängd
            print("nya saldot är: " + str(saldo))