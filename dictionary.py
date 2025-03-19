class Dictionary:

    def __init__(self):
        self.dizionario = None

    def loadDictionary(self, path, dizionario=None):
        if dizionario is None:
            dizionario = []
        infile = open(path, "r", encoding="utf-8")
        riga = infile.readline()
        while len(riga) != 0:
            riga = riga.strip()
            dizionario.append(riga)
            riga = infile.readline()
        infile.close()
        self.dizionario = dizionario

    def printAll(self):
        for parola in self.dizionario:
            print(parola)

    @property
    def dict(self):
        return self._dict