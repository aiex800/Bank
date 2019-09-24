registernamn = input("registrera användarnamn: ")
registerlösen = input("registrera lösenord: ")
saldo = float(input("hur mycke pengar har du? "))



while True:
    namn = input("användarnamn: ")
    lösen = input("lösenord: ")
    if namn != registernamn:
        print("Fel användarnamn")

    elif namn == registernamn:
        print(" ")

    if lösen != registerlösen:
        print("fel lösenord: ")

    elif lösen == registerlösen:
        print("hej " + namn)
        print("ditt saldo är: " + str(saldo))
        insättning = input("vill du ta ut eller sätta in pengar: ")
        mängd = float(input("Hur mycket? "))
        if insättning == "sätta in":
            saldo = mängd + saldo
            print("nya saldot är: " + str(saldo))
        elif insättning == "ta ut":
            saldo = mängd - saldo
            print("nya saldot är: " + str(saldo))