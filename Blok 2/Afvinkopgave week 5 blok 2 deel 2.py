# auteur  : Armin van Eldik
# nummer  : 618604
# DOC     : 12-12-2018
# opdracht: afvinkopdracht 5 blok 2 deel 2
# klas    : BIN-1B


def main():
    file = 'Felis_catus.Felis_catus_8.0.cdna.all.fasta'
    headers, sequenties = openfile(file)
    objlistgc = cglistmaker(sequenties)
    longestfilter(objlistgc, headers, sequenties)


def openfile(filename):
    """opent de file en maakt er 2 lijsten van
    :param filename:
    naam van de file
    :return:
    returned 2 lijsten, van de headers en van de sequenties
    """
    headers = []
    sequenties = []
    linetemp = ''
    file = open(filename, 'r')
    for line in file:
        line = line.strip('\n')
        if line.startswith('>'):
            headers.append(line)
            if not linetemp == '':
                sequenties.append(linetemp)
            linetemp = ''
        else:
            if not line.startswith('>'):
                linetemp += line
    return headers, sequenties
# file = filenaam
# headers = lijst met de headers uit de file
# sequenties = lijst van de sequenties uit de file
# linetemp = tijdelijke opslag voor elke sequentiestring


def cglistmaker(sequenties):
    """vraagt van elke sequentie het CG percentage en zet het in een lijst
    :param sequenties:
    lijst met sequenties
    :return:
    lijst met CG%'s
    """
    cglist = []
    for x in range(len(sequenties)):
        dnaclass = DNA(sequenties[x])
        cglist.append(dnaclass.getGC())
    return cglist
# cglist = lijst waar de CG%'s opgeslagen worden


def longestfilter(cglist, helist, selist):
    """vraagt de data op uit de class
    :param cglist:
    lijst van CG%'s
    :param helist:
    lijst van Headers
    :param selist:
    lijst van sequenties
    :return:
    prints van:
    hoogste CG% van de sequentie
    welke sequentie (header + volgorde)
    transcript van de sequentie
    lengte van de sequentie
    """
    cgpos = cglist.index(max(cglist))
    print('highest CG% of', max(cglist), '% found in :')
    print(helist[cgpos])
    dnaclass = DNA(selist[cgpos])
    print('DNA:\n'+dnaclass.getSequentie())
    print('RNA:\n'+dnaclass.getTranscript())
    print('lengte van de sequentie :', len(dnaclass.getSequentie()))
# cgpos = postie in de lijst met het hoogste CG%(hoogste interger)
# dnaclass = aanroep van de class


class DNA:
    def __init__(self, initobject):
        """checked of het object bgeint met > (header of sequentie)
        :param initobject:
        header of sequentie
        """
        if initobject.startswith('>'):
            self.setHeader(initobject)
        else:
            self.setSequentie(initobject)

    def setSequentie(self, setsequentie):
        """set de sequentie
        :param setsequentie:
        input uit de init
        :return:
        gesette sequentie
        """
        self.sequentie = setsequentie

    def getSequentie(self):
        """returned de sequentie die geset is
        :return:
        gesette sequentie
        """
        return self.sequentie

    def setHeader(self, setHeader):
        """set de header
        :param setHeader:
        input uit init
        :return:
        gesette header
        """
        self.header = setHeader

    def getHeader(self):
        """returned de header
        :return:
        gesette header
        """
        return self.header

    def getTranscript(self):
        """transcripeerd de DNA naar RNA
        :return:
        DNA maar T = U
        """
        return self.sequentie.replace('T', 'U')

    def getGC(self):
        """berekend het GC%
        :return:
        GC%
        """
        CG = 0
        for character in self.sequentie:
            if character in ['C', 'G']:
                CG += 1
        CGperc = CG / len(self.sequentie)
        return round(CGperc*100, 2)


main()