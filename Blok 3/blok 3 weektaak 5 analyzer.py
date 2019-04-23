# auteur  : Armin van Eldik
# nummer  : 618604
# DOC     : 13-03-2019
# opdracht: Blok 3 weektaak 5 opdracht 3 stap 5 deel 2
# klas    : BIN-1A
# functie : leest bestand en maakt daar een histogram van
import matplotlib.pyplot as plt
import statistics

def dictmaker():
    """creates a dictionary with key = % and value = amount
    :return: dictionary with keys 0-50, empty values
    """
    dict = {}
    for i in range(50):
        dict[str(i)] = 0
    return dict


def analyzer(dict, file):
    """iterates over dict; iterates over file, stripping \n and splitting on 100.00, list of 2 is returned;
    iterates over 2nd column, splits on [space];iterates over values, if value between key and key+1 of dict it counts.
    :param dict: dictionary returned from dictmaker
    :param file: ClustalO file (modified; all spaces are 1, top info is deleted.)
    :return: dictionary of amounts in each % bracket
    """
    raw_values=[]
    for key in dict:
        for line in file:
            line = line.strip('\n').split('100.00 ')
            try:
                line = line[1]
                for val in line.split(' '):
                    raw_values.append(float(val))
                    if int(key) <= float(val) <= int(key)+1:
                        dict[key] += 1
            except IndexError:
                pass
    return dict, raw_values


def cg_med_calc(dict):
    return statistics.median(dict)

def cg_var_calc(dict):
    return statistics.pvariance(dict)

def mpl(dict,raw_values):
    plt.title('% identity in randomized HIV1, HIV2, SIV SIVmnd2 sequences')
    plt.xlabel('% match (amounts are between its and the next entry)')
    plt.ylabel('amount of matches in each % bracket')
    plt.bar(list(dict.keys()), list(dict.values()))
    plt.annotate('Variance: {}, median: {}'.format(round(cg_var_calc(raw_values), 2),
                                                   cg_med_calc(raw_values)),
                 xy=(0.01, 0.97), xycoords='axes fraction', fontsize=7)
    plt.xticks(rotation=90, fontsize=8)
    plt.show()


def main():
    file = openfile()
    dict = dictmaker()
    dict_val, raw_val = analyzer(dict, file)
    mpl(dict_val, raw_val)


def openfile():
    filename = 'ClustalO results.txt'
    file = open(filename).readlines()
    return file


main()
