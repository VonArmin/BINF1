# auteur  : Armin van Eldik
# nummer  : 618604
# DOC     : 19-02-2019
# opdracht: Blok 3 weektaak 3 opdracht 3
# klas    : BIN-1A
# functie : kijkt per aminozuur hoe vaak elk codon ervan voorkomt
import matplotlib.pyplot as plt
import numpy as np
import re


def codon_analyse(seq):
    aa3 = {"Ala": {"GCT": 0, "GCC": 0, "GCA": 0, "GCG": 0},
           "Arg": {"CGT": 0, "CGC": 0, "CGA": 0, "CGG": 0, "AGA": 0, "AGG": 0},
           "Asn": {"AAT": 0, "AAC": 0},
           "Asp": {"GAT": 0, "GAC": 0},
           "Cys": {"TGT": 0, "TGC": 0},
           "Gln": {"CAA": 0, "CAG": 0},
           "Glt": {"GAA": 0, "GAG": 0},
           "Gly": {"GGT": 0, "GGC": 0, "GGA": 0, "GGG": 0},
           "His": {"CAT": 0, "CAC": 0},
           "Ile": {"ATT": 0, "ATC": 0, "ATA": 0},
           "Let": {"TTA": 0, "TTG": 0, "CTT": 0, "CTC": 0, "CTA": 0, "CTG": 0},
           "Lys": {"AAA": 0, "AAG": 0},
           "Met": {"ATG": 0},
           "Phe": {"TTT": 0, "TTC": 0},
           "Pro": {"CCT": 0, "CCC": 0, "CCA": 0, "CCG": 0},
           "Ser": {"TCT": 0, "TCC": 0, "TCA": 0, "TCG": 0, "AGT": 0, "AGC": 0},
           "Thr": {"ACT": 0, "ACC": 0, "ACA": 0, "ACG": 0},
           "Trp": {"TGG": 0},
           "Tyr": {"TAT": 0, "TAC": 0},
           "Val": {"GTT": 0, "GTC": 0, "GTA": 0, "GTG": 0},
           "Stop": {"TAG": 0, "TGA": 0, "TAA": 0}}
    codon_amounts = {}
    loc = 0
    frame = 3

    for place in range(int((len(seq)/frame))):
        try:
            codon_amounts[seq[loc:loc+frame].upper()] += 1
        except KeyError:
            codon_amounts[seq[loc:loc+frame].upper()] = 1
        loc += frame
    # itereerd over de sequentie en maakt een entry in codon_amounts dictionary met key=codon, value=hoeveelheid
    # wanneer niet in de dictionary, wordt er een nieuwe key toegevoegd

    for amino_acid in aa3:
        for codon in aa3[amino_acid]:
            if codon_amounts.get(codon):
                aa3[amino_acid][codon] = codon_amounts.get(codon)
    # itereerd over lege (hardcoded) dictionary en neemt de waardes uit de codon_amounts dictionary over
    # in principe wordt hier het codon aan een aminozuur gekoppeld.

    for amino_acid in aa3:
        aa_amount = (sum(list(aa3[amino_acid].values())))
        for codon in aa3[amino_acid]:
            aa3[amino_acid][codon] = round(aa3[amino_acid][codon]/aa_amount*100)
    # itereerd over gevulde dictionary en veranderd de waardes naar procenten ipv hoeveelheden.

    return aa3


def mat_plot_lib(dataset, name):
    for aa in dataset:
        # plt.figure()
        try:
            plt.title(name+'\nenvelope sequence', fontsize=12)
            plt.xlabel('Codon')
            plt.ylabel('% of each codon')
            plt.bar(list(dataset[aa].keys()), list(dataset[aa].values()), align='center', label=[aa])
            plt.legend(fontsize=12, loc=0, bbox_to_anchor=(-0.075, 0.9), framealpha=0)
            plt.xticks(fontsize=10, rotation=90)
        except TypeError:
            print('Type error')
    # plt.savefig('{} plot all nt.png'.format(name), format='png')
    plt.show()


def main():
    seq, name = open_read_file()
    dataset = codon_analyse(seq)
    mat_plot_lib(dataset, name)


def open_read_file():
    name = 'HIV_2_env.txt'
    orgname = name.strip('.txt').strip('.fasta')
    try:
        file = open(name, 'r')
        string_seq = ''
        for line in file:
            #orgname = re.search('[A-Z]{1}[a-z]* [a-z]*', name).group()
            if line.isupper():
                string_seq += line.strip('\n').strip('N')
        return string_seq, orgname
    except FileNotFoundError:
        print('File not found')


main()
