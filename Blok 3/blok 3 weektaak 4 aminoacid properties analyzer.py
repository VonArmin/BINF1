# auteur  : Armin van Eldik
# nummer  : 618604
# DOC     : 26-02-2019
# opdracht: Blok 3 weektaak 4 opdracht 1 onderzoekopdracht 2
# klas    : BIN-1A
# functie : berekend de hoeveelheid aminozouren in een sequentie en drukt deze uit in verschillende plots
import matplotlib.pyplot as plt
import numpy as py


def aa_counter(file):
    aa_amounts = {}
    for line in file:
        if not line.startswith('>'):
            line = line.strip('\n')
            for aa in line:
                try:
                    aa_amounts[aa] += 1
                except KeyError:
                    aa_amounts[aa] = 1
    return aa_amounts


def aa_phil_phob(aa_percs):
    hydrophobicity = {}
    hydrophobic_aa = ['G', 'P', 'F', 'A', 'I', 'L', 'V']
    hydrophobic_amount = 0
    hydrophilic_aa = ['S', 'T', 'D', 'E', 'C', 'N', 'Q', 'R', 'H']
    hydrophilic_amount = 0
    for aa in aa_percs:
        if aa in hydrophilic_aa:
            hydrophilic_amount += aa_percs[aa]
        if aa in hydrophobic_aa:
            hydrophobic_amount += aa_percs[aa]
    hydrophobicity['hydrophobic'] = hydrophobic_amount
    hydrophobicity['hydrophilic'] = hydrophilic_amount
    return hydrophobicity


def aa_percs(aa_amounts):
    aa_percs = {'T': 0, 'C': 0}
    for aa in aa_amounts.keys():
        aa_percs[aa] = round(aa_amounts.get(aa)/sum(aa_amounts.values())*100, 2)
    return aa_percs
# T and C are defined so it wont give an error when they are not in the sequence when called in main function

def aa_least(aa_percs):
    aa_least_percs = {}
    aa_percs_val = list(aa_percs.values())
    aa_percs_aa = list(aa_percs.keys())
    for index in py.argsort(aa_percs_val)[:3]:
        aa_least_percs[aa_percs_aa[index]] = aa_percs_val[index]
    return aa_least_percs


def aa_max(aa_percs):
    aa_max_percs = {}
    aa_percs_val = list(aa_percs.values())
    aa_percs_aa = list(aa_percs.keys())
    for index in py.argsort(aa_percs_val)[-3:]:
        aa_max_percs[aa_percs_aa[index]] = aa_percs_val[index]
    return aa_max_percs


def mpl_cthydro(cys, trp, aa_max, aa_least, hydrophobicity, name):
    plt.title('{}\nlowest and highest %\'s of AA\'s'.format(name) )
    plt.bar(list(aa_least.keys()), list(aa_least.values()),label='lowest %')
    plt.bar(list(aa_max.keys()), list(aa_max.values()),label='highest %')
    plt.annotate('trp: {}%, cys: {}%'.format(str(trp), str(cys)), xy=(0.02, 0.82), xycoords='axes fraction')
    plt.legend()
    plt.savefig('{} AA plot.png'.format(name))
    plt.figure()
    plt.title('{}\nHydrophobicity in %\'s'.format(name))
    plt.bar(list(hydrophobicity.keys()), list(hydrophobicity.values()), label='hydrophobic aa\'s')
    plt.savefig('{} hydro plot.png'.format(name))


def main():
    file, orgname = open_file()
    aa_amounts = aa_counter(file)
    aa_percentages = aa_percs(aa_amounts)
    hydrophobicity = aa_phil_phob(aa_percentages)
    mpl_cthydro(aa_percentages['C'], aa_percentages['T'], aa_max(aa_percentages),
                aa_least(aa_percentages), hydrophobicity, orgname)


def open_file():
    file_name = 'Transmembrane TGFBR1 prot hs.fasta'
    name = file_name.strip('.txt').strip('.fasta')
    file = open(file_name).readlines()
    return file, name


main()
