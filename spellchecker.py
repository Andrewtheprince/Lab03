import time as t
import multiDictionary
md = multiDictionary.MultiDictionary()

class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        txtIn = replaceChars(txtIn)
        print("______________________________")
        print("Using contains")
        tempo0 = t.time()
        paroleSbagliate = md.searchWord(txtIn, language)
        tempo1 = t.time()
        for parola in paroleSbagliate:
            print(parola)
        print(f"Time elapsed {tempo1-tempo0}")
        print("______________________________")
        print("Using Linear search")
        tempo2 = t.time()
        paroleSbagliate2 = md.searchWordLinear(txtIn, language)
        tempo3 = t.time()
        for parola in paroleSbagliate2:
            print(parola)
        print(f"Time elapsed {tempo3 - tempo2}")
        print("______________________________")
        print("Using Dichotomic search")
        tempo4 = t.time()
        paroleSbagliate3 = md.searchWordDichotomic(txtIn, language)
        tempo5 = t.time()
        for parola in paroleSbagliate3:
            print(parola)
        print(f"Time elapsed {tempo5 - tempo4}")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\@#?=)(/&%$£!|,.-_:;+*^[]{}<>"
    for c in chars:
        text = text.replace(c, "")
    return text.lower()