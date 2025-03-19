import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input()
    control = False
    while not control:
        if (txtIn == "1") or (txtIn == "2") or (txtIn == "3") or (txtIn == "4"):
            control = True
        else:
            print("Puoi inserire solo un numero da 1 a 4!")
            txtIn = input()

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        sc.handleSentence(txtIn,"italian")
        continue

    elif int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        sc.handleSentence(txtIn,"english")
        continue

    elif int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        sc.handleSentence(txtIn,"spanish")
        continue

    elif int(txtIn) == 4:
        break


