import dictionary as d
import richWord as rw

class MultiDictionary:

    def __init__(self):
       self.dicItaliano = d.Dictionary()
       self.dicItaliano.loadDictionary("resources/Italian.txt")
       self.dicInglese = d.Dictionary()
       self.dicInglese.loadDictionary("resources/English.txt")
       self.dicSpagnolo = d.Dictionary()
       self.dicSpagnolo.loadDictionary("resources/Spanish.txt")

    def printDic(self, language):
        if language == "italian":
            self.dicItaliano.printAll()
        elif language == "english":
            self.dicInglese.printAll()
        else:
            self.dicSpagnolo.printAll()

    def searchWord(self, words, language):
        parole = words.split(" ")
        paroleSbagliate = []
        if language == "italian":
            for parola in parole:
                if parola not in self.dicItaliano.dizionario:
                    word = rw.RichWord(parola)
                    paroleSbagliate.append(word)
        elif language == "english":
            for parola in parole:
                if parola not in self.dicInglese.dizionario:
                    word = rw.RichWord(parola)
                    paroleSbagliate.append(word)
        else:
            for parola in parole:
                if parola not in self.dicSpagnolo.dizionario:
                    word = rw.RichWord(parola)
                    paroleSbagliate.append(word)
        return paroleSbagliate

    def searchWordLinear(self, words, language):
        parole = words.split(" ")
        paroleSbagliate = []
        if language == "italian":
            for parola in parole:
                trovato = False
                for elemVoc in self.dicItaliano.dizionario:
                    if elemVoc == parola:
                        trovato = True
                        break
                if not trovato:
                    word = rw.RichWord(parola)
                    paroleSbagliate.append(word)
        elif language == "english":
            for parola in parole:
                trovato = False
                for elemVoc in self.dicInglese.dizionario:
                    if elemVoc == parola:
                        trovato = True
                        break
                if not trovato:
                    word = rw.RichWord(parola)
                    paroleSbagliate.append(word)
        else:
            for parola in parole:
                trovato = False
                for elemVoc in self.dicSpagnolo.dizionario:
                    if elemVoc == parola:
                        trovato = True
                        break
                if not trovato:
                    word = rw.RichWord(parola)
                    paroleSbagliate.append(word)
        return paroleSbagliate

    def searchWordDichotomic(self, words, language):
        parole = words.split(" ")
        paroleSbagliate = []
        if language == "italian":
            numParoleVocabolario = len(self.dicItaliano.dizionario)
            if numParoleVocabolario % 2 == 0:
                elementoCentrale = numParoleVocabolario / 2
            else:
                elementoCentrale = (numParoleVocabolario + 1) / 2
            parolaCentrale = self.dicItaliano.dizionario[int(elementoCentrale)]
            for parola in parole:
                verifica = False
                if parola == parolaCentrale:
                    verifica = True
                else:
                    if parola[0] < parolaCentrale[0]:
                        for i in range(0, int(elementoCentrale), -1):
                            if self.dicItaliano.dizionario[i] == parola:
                                verifica = True
                                break
                    else:
                        for i in range(int(elementoCentrale), numParoleVocabolario):
                            if self.dicItaliano.dizionario[i] == parola:
                                verifica = True
                                break
                if not verifica:
                    word = rw.RichWord(parola)
                    paroleSbagliate.append(word)
        elif language == "english":
            numParoleVocabolario = len(self.dicInglese.dizionario)
            if numParoleVocabolario % 2 == 0:
                elementoCentrale = numParoleVocabolario / 2
            else:
                elementoCentrale = (numParoleVocabolario + 1) / 2
            parolaCentrale = self.dicInglese.dizionario[int(elementoCentrale)]
            for parola in parole:
                verifica = False
                if parola == parolaCentrale:
                    verifica = True
                else:
                    if parola[0] < parolaCentrale[0]:
                        for i in range(0, int(elementoCentrale), -1):
                            if self.dicInglese.dizionario[i] == parola:
                                verifica = True
                                break
                    else:
                        for i in range(int(elementoCentrale), numParoleVocabolario):
                            if self.dicInglese.dizionario[i] == parola:
                                verifica = True
                                break
                if not verifica:
                    word = rw.RichWord(parola)
                    paroleSbagliate.append(word)
        else:
            numParoleVocabolario = len(self.dicSpagnolo.dizionario)
            if numParoleVocabolario % 2 == 0:
                elementoCentrale = numParoleVocabolario / 2
            else:
                elementoCentrale = (numParoleVocabolario + 1) / 2
            parolaCentrale = self.dicSpagnolo.dizionario[int(elementoCentrale)]
            for parola in parole:
                verifica = False
                if parola == parolaCentrale:
                    verifica = True
                else:
                    if parola[0] < parolaCentrale[0]:
                        for i in range(0, int(elementoCentrale), -1):
                            if self.dicSpagnolo.dizionario[i] == parola:
                                verifica = True
                                break
                    else:
                        for i in range(int(elementoCentrale), numParoleVocabolario):
                            if self.dicSpagnolo.dizionario[i] == parola:
                                verifica = True
                                break
                if not verifica:
                    word = rw.RichWord(parola)
                    paroleSbagliate.append(word)
        return paroleSbagliate
