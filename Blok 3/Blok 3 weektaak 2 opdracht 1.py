# auteur  : Armin van Eldik
# nummer  : 618604
# DOC     : 12-02-2019
# opdracht: Blok 3 weektaak 2 opdracht 1
# klas    : BIN-1A
# functie : berekend het GC percentage van sequenties en maakt daar een plot van
import re
import matplotlib.pyplot as plt
import statistics


def cg_avg_calc(string_seq):
    try:
        return round(len(re.findall('[CG]', string_seq))/len(string_seq)*100, 2)
    except ZeroDivisionError:
        return 'N/A'


def cg_med_calc(cg_perc):
    return statistics.median(cg_perc)


def cg_var_calc(cg_perc):
    return statistics.pvariance(cg_perc)


def cg_analyse(string_seq):
    frame = int(input('enter the length of the frame in an integer (not 1):'))
    frameplace = 0
    seq_len = len(string_seq)
    cg_perc = []
    try:
        for num in range(int(((seq_len-(seq_len % frame)) / frame))):
            cg_perc.append(round((len(re.findall('[CG]', string_seq[frameplace:frameplace + frame]))/frame*100), 2))
            frameplace += frame
        cg_perc.append(round(len(re.findall
                             ('[CG]', string_seq[seq_len-(seq_len % frame):seq_len]))/(seq_len % frame)*100, 2))
    except ZeroDivisionError:
        print('Division error, Frame can\'t be 1.')
    # this re expression finds the GC% between the (total length-modulo of length) : total length (slice)
    # (the last frame of the sequence)
    return cg_perc, str(frame)


def mat_plot_lib(cg_perc, cg_med, cg_var, cg_avg, frame, org_name):
    plt.plot(cg_perc, linewidth=0.5, label='GC%')
    plt.axhline(cg_med, color='red', label='Median', linewidth=0.5)
    plt.axhline(cg_avg, color='blue', label='Average', linewidth=0.5)
    plt.title(org_name)
    plt.annotate(('variance : {}, Median : {}, Average : {}, stepsize : {}, max : {}, min : {}'
                  .format(str(round(cg_var, 2)), str(cg_med), str(cg_avg), str(frame), max(cg_perc), min(cg_perc))),
                 xy=(0.01, 0.01), xycoords='axes fraction', fontsize=7)
    plt.ylabel('GC%')
    plt.xlabel('position (nt * stepsize)')
    plt.legend(fontsize=7, loc=1)
    # plt.savefig('plot {}, frame {}.png'.format(str(org_name), str(frame)), format='png')
    plt.show()


def main():
    string, org_name = open_read_file()
    ask = True
    while ask:
        cg_perc, frame = cg_analyse(string)
        mat_plot_lib(cg_perc, cg_med_calc(cg_perc), cg_var_calc(cg_perc), cg_avg_calc(string), frame, org_name)
        if input('Rerun with another frame? y/n') == 'n':
            ask = False


def open_read_file():
    try:
        file = open('Heliobacter canadensis complete record.fasta', 'r')
        string_seq = ''
        name = 'no name found'
        for line in file:
            if line.startswith('>'):
                name = re.search('[A-Z]{1}[a-z]* [a-z]*', line).group()
            if line.isupper():
                string_seq += line.strip('\n').strip('N')
        return string_seq, name
    except FileNotFoundError:
        print('File not found')



main()
