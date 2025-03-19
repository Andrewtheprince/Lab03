import time as t
import multiDictionary
md = multiDictionary.MultiDictionary()

class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        txtIn = replaceChars(txtIn)
        tempo0 = t.time()
        paroleSbagliate = md.searchWord(txtIn, language)
        tempo1 = t.time()
        print("______________________________")
        for parola in paroleSbagliate:
            print(parola)
        print(f"Time elapsed {tempo1-tempo0}")


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