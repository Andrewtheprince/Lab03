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

