# auteur  : Armin van Eldik
# nummer  : 618604
# DOC     : 08-01-2019
# opdracht: afvinkopdracht 6 blok 2 deel 2
# klas    : BIN-1B

def main():
    caller()

def caller():
    """opent de file en roept de stringcr functie aan
    :return: print of het dna is of niet
    """
    file = open('Felis_catus.Felis_catus_8.0.cdna.all.fasta','r')
    # file = open('test.fasta','r')
    check = isDNA(stringcr(file))
    if check:
        print('het is DNA')
    if check is False:
        print('het is geen DNA')
# file = naam van de file en leesmodus
# check = true of false wanneer dat uit isDNA gereturned wordt


def stringcr(sequence):
    """loopt over elke regel heen en roept bij elke regel de functie isDNA aan als hij niet start met >
    :param sequence: dna sequentie
    :return: True als het DNA is, False als het geen DNA is
    """
    check = True
    for line in sequence:
        if not line.startswith('>'):
            check = isDNA(line)
        if check is False:
            return False
    if check is True:
        return True

def isDNA(dna):
    """accepteerd een string en tetourneerd True waneer hij door de regel heen is gelopen, False wanneer het geen \n '' A T C G of N is
    :param dna: string uit functie stringcr
    :return: True wanneer het \n '' ATCG of N is
             False wanneer het niet "       "
    """
    print(dna)
    if dna == '\n' or dna == '':
        return True
    elif dna is True:
        return True
    elif dna is False:
        return False
    elif dna[0] in 'ATCGN':
        return isDNA(dna[1:])
    else:
        return False

main()