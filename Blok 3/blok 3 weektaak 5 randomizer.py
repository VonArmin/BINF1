# auteur  : Armin van Eldik
# nummer  : 618604
# DOC     : 12-03-2019
# opdracht: Blok 3 weektaak 5 opdracht 3 stap 5 deel 1
# klas    : BIN-1A
# functie : schud de sequentie en zet deze in een file
import random


def randomizer(sequence):
    random.shuffle(sequence)
    return sequence


def writer(name, sequence, header):
    """iterates over amount of shuffles and, for each shuffles writes a shuffled sequence to the file
    :param name: string name of the HIV variant
    :param sequence: list of the full sequence
    :param header: string of header
    :return: writes randomized sequnces to file
    """
    shuffles = 100
    filename = 'randomized {} - {} times.fasta'.format(name, shuffles)
    file = open(filename, 'w')
    file = open(filename, 'a')
    for shuffle in range(shuffles):
        file.write(header.replace('>lcl|', '>lclSH{}SIV| SH{} '.format(shuffle+1, shuffle+1))+'\n')
        randomizer(sequence)
        file.write(''.join(sequence)+'\n')


def main():
    name, sequence, header = openfile()
    writer(name, sequence, header)


def openfile():
    """opens the file and makes a list of the sequence as opposed to a string
    :return:list of sequence
    """
    sequence = []
    filename = 'SIVmnd2 proteins - env.txt'
    name = filename.strip('.txt').strip('.fasta')
    file = open(filename).readlines()
    for line in file:
        line = line.strip('\n')
        if line.startswith('>'):
            header = line
        if line.isupper():
            for character in line:
                sequence.append(character)
    return name, sequence, header


main()
