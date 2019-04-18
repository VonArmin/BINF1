# auteur  : Armin van Eldik
# nummer  : 618604
# DOC     : 04-12-2018
# opdracht: afvinkopdracht 4 blok 2
# klas    : BIN-1B
import re
import time


def main():
    filechrom = 'Mus_musculus.GRCm38.dna.chromosome.1.fasta'
    fileprot = 'Mus_musculus.GRCm38.pep.all.fasta'
    filecoli = 'E_coli.fasta'
    paterncheck(fileprot)
    aachecker(fileprot)
    if input('wil je de functie dnacheck uitvoeren? y/n') == 'y':
        dnacheck(filechrom)
    if input('wil je de functie fordnacheck uitvoeren? y/n') == 'y':
        fordnacheck(filechrom)
    analyzer(filecoli)


def paterncheck(fileprot):
    """deze fuctie kijkt of de RE in de sequentie voorkomt
    :param fileprot:
    bestandsnaam
    :return:
    print van elke seq waar de RE in voorkomt
    """
    prot = '(MCNSSC[MV]GGMNRR)'
    fileprot = open(fileprot, 'r')
    for line in fileprot:
        if line.startswith('>'):
            title = line
        if not line.startswith('>'):
            match = re.search(prot, line)
            if match:
                print('gevonden in:', title, 'index-positie van concensus patroon:', match.start())
                print(line)
    fileprot.close()


def aachecker(fileprot):
    """deze functie kijkt of de seq niet uit niet-AA's bestaat.
    :param fileprot:
    bestandsnaam
    :return:
    print van de hoeveelheid checkte lines
    """
    aafilter = '(.*[ARNDCFQEGHILKMPSTWYV].*)'
    fileprot = open(fileprot, 'r')
    readlines = 0
    matches = 0
    for line in fileprot:
        if not line.startswith('>'):
            line = line.strip('\n')
            filter = re.search(aafilter, line, )
            filter = filter.group()
            readlines += 1
            if filter != line:
                print('geen match', print(filter, line))
            if filter == line:
                matches += 1
    print('lines read:', readlines)
    print('matches:', matches)
    print('matching % :', round(matches/readlines*100, 2), '%\n')
    fileprot.close()


def dnacheck(filechrom):
    """deze functie checked of er iets anders dan ATCG in zit dmv regular expressions
    :param filechrom:
    :return:
    file bestaat alleen uit ATCG of niet alleen uit ATCG
    started/finished times
    """
    dnafilter = '^[ATCG]'
    filechrom = open(filechrom, 'r')
    filechrom.read()
    filechrom.readlines(1)
    localtime1 = time.asctime(time.localtime(time.time()))
    match = re.search(dnafilter, filechrom)
    if match is None:
        print('file bevat alleen ATCG')
    elif match:
        print('file bevat ergens geen ATCG')
    localtime2 = time.asctime(time.localtime(time.time()))
    print('met RE checken:')
    print("started  :", localtime1)
    print("finished :", localtime2)
    filechrom.close()


def fordnacheck(filechrom):
    """deze functie checked of er iets anders dan ATCG in zit dmv for loop
    :param filechrom:
    :return:
    started/finished tijd
    als het geen DNA is
    """
    dna = ['A', 'T', 'C', 'G', '\n', 'N']
    filechrom = open(filechrom, 'r')
    localtime1 = time.asctime(time.localtime(time.time()))
    print('met for loop checken:')
    print("started  :", localtime1)
    for line in filechrom:
        if not line.startswith('>'):
            for character in line:
                if character not in dna:
                    print(character, 'karakter niet in de lijst (geen DNA)')
    localtime2 = time.asctime(time.localtime(time.time()))
    print('met for loop checken:')
    print("finished :", localtime2)
    filechrom.close()


def analyzer(filecoli):
    """in theorie zoekt deze funtie het promotor gen in de sequentie van e coli
    :param filecoli:
    :return:
    wel of geen match van prot in de e coli seq, zo ja, waar
    """
    prot1 = 'ggcacgtaaacaactaacggacaattctacctaaca'.upper()
    prot2 = 'tgtaagtttatacataggcgagtactctgttatgg'.upper()
    refcheck = 'CCGGAACAAATTGAACAATCCTACGCCAG'.upper()
    file = open(filecoli, 'r')
    recheck = re.search(refcheck, file.read())
    match2 = re.search(prot1, file.read())
    match3 = re.search(prot2, file.read())
    if recheck:
        print('refcheck', refcheck, 'op', recheck.start())
    if recheck is None:
        print(refcheck, 'niet gevonden')
    if match2:
        print(prot1, 'op', match2.start())
    if match2 is None:
        print(prot1, 'niet gevonden')
    if match3:
        print(prot2, 'op', match3.start())
    if match3 is None:
        print(prot2, 'niet gevonden')
    return


main()
