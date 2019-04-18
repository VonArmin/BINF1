# auteur  : Armin van Eldik
# nummer  : 618604
# DOC     : 11-12-2018
# opdracht: afvinkopdracht 5 blok 2 deel 1
# klas    : BIN-1B


def main():
    seq = DNA('ACATAAGATATAGAGA')
    print(seq.getDNA())
    print(seq.getTranscript())
    print(seq.getLength())
    print(seq.getGC())
    seq.setDNA('ATACAGACAGAACAG')
    print(seq.getDNA())
    print(seq.getTranscript())
    print(seq.getLength())
    print(seq.getGC())

class DNA:
    def __init__(self, dnaseq):
        self.setDNA(dnaseq)

    def setDNA(self, DNAstring):
        self.seq = DNAstring

    def getDNA(self):
        return self.seq

    def getTranscript(self):
        return self.seq.replace('T', 'U')

    def getLength(self):
        return len(self.seq)

    def getGC(self):
        rna = ['C', 'G']
        gc = 0
        for character in self.seq:
            if character in rna:
                gc += 1
        return round(gc/len(self.seq)*100, 2)


main()
