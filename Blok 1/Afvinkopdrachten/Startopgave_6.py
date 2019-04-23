# Auteur:Armin van Eldik
# Datum:14-11-2018
# Versie:1
# funtie: checken of een enzym in de sequentie knipt.


def main():
    try:
        bestand = open('Alpaca RNA.fasta').readlines()
        zoekwoord = input("Geef een zoekwoord op: ")
        headers, seqs = lees_inhoud(bestand)
        for x in range(len(headers)):
            if zoekwoord in headers[x]:
                if is_dna(seqs[x]):
                    print(headers[x])
                    knipt(seqs[x])
    except FileNotFoundError:
        print('Geen file gevonden, controleer of de file aanwezig is.')
    except IOError:
        print('algemene IO error')


def lees_inhoud(bestand):
    """'leest de inhoud van het bestand

    Input:
    bestand

    Output:
    headers - een lijst van elke header in het bestand.
    seqs - lijst van elke sequentie.
    """
    headers = []
    seqs = []
    seq = ""
    for line in bestand:
        line = line.strip()
        if ">" in line:
            if seq != "":
                seqs.append(seq)
                seq = ""
            headers.append(line)
        else:
            seq += line.strip()
    seqs.append(seq)
    return headers, seqs


def is_dna(seq):
    """checked of het bestand een DNA is.

    Input:
    seq - sequentie uit leesinhoud

    Output:
    False - als het geen DNA is
    True - als het wel DNA is
    """
    dnacodons = ['A', 'T', 'C', 'G']
    for letter in seq:
        if not letter.startswith('\n'):
            if letter not in dnacodons:
                print(letter, 'False')
                return False
    return True


def knipt(sequentie):
    """'Checked of een enzym in de sequentie zit(knipt).

    Input:
    sequentie - Goedgekeurde DNA sequentie.

    Output:
    Print welke enzymen knippen in de sequentie.
    """
    try:
        bestand = open("enzymen.txt").readlines()
        for regel in bestand:
            enzym, seq = regel.split()
            seq = seq.replace("^", "")
            if seq in sequentie:
                print(enzym, 'knipt')
    except FileNotFoundError:
        print('file met enzymen is niet aanwezig.')
        main()
    except IOError:
        print('algemene IO error.')


main()
