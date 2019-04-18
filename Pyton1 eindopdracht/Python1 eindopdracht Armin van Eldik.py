# auteur  : Armin van Eldik
# nummer  : 618604
# datum   : 8-11-2018
# opdracht: eindopdracht blok 1 Python
# klas    : BIN-1B


def main():
    try:
        bestandsnaam = 'chr1.csv'
        print('aantal genen in bestand :', aantal_genen(bestandsnaam))
        print('aantal genen met een GC% goter dan 50% :', groter_gc_perc_dan(bestandsnaam))
        print('gemiddelde lengte van de sequenties :', gemiddelde_lengte(bestandsnaam))

    except UnboundLocalError:
        print('Variabele voor de assignment(geen variabele)')
# roept alle andere fucties aan
# maakt een variabele om het makkelijker te maken de file te openen


def aantal_genen(bestandsnaam):
    try:
        bestand = open(bestandsnaam, 'r')
        genen = 0
        for regel in bestand:
            if not regel.startswith('Gene'):
                genen += 1
    except FileNotFoundError:
        print('bestand niet gevonden')
    return genen
# opent het bestand
# voor elke regel in het bestand; genen + 1


def groter_gc_perc_dan(bestandsnaam, gc_perc=50):
    try:
        bestand = open(bestandsnaam, 'r')
        GroterDan50 = 0
        for regel in bestand:
            if not regel.startswith('Gene'):
                regel = regel.split('\t')
                regel[5] = regel[5].replace('\n', '')
                if float(regel[5]) > gc_perc:
                    GroterDan50 += 1
    except IndexError:
        print('index out of range')
    except FileNotFoundError:
        print('bestand niet gevonden')
    return GroterDan50
# als de regel niet start met Gene gaat het script door
# de regel wordt gesplitst in kolommen
# in de 6e kolom (index 5) staat het GC% er wordt dus alleen naar deze kolom gekeken
# \n wordt vervangen door niets (anders kan het niet in een float gezet worden)
# (kan inderdaad ook met rstrip, maar op mijn manier heb ik er zelf over nagedacht) )
# als het GC% groter is wordt het geteld, anders niet


def gemiddelde_lengte(bestandsnaam):
    try:
        bestand = open(bestandsnaam, 'r')
        totlen = 0
        totgene = 0
        for regel in bestand:
            if not regel.startswith('Gene'):
                regel = regel.split('\t')
                lengte = int(regel[4]) - int(regel[3])
                totlen += lengte
                totgene += 1
        gemlengte = round(totlen / totgene, 2)
    except IndexError:
        print('index out of range')
    except IOError:
        print('algemene IO error(geen variabele)')
    except ZeroDivisionError:
        print('er wordt door 0 gedeeld!')
    return gemlengte


# alle lengtes worden eerst bij elkaar opgeteld door kolom 5 en 4 van elkaar af te halen
# er wordt een variabale aangemakt om later door te delen om de gemiddelde lengte vast te stellen
# return de gemlengte

main()
