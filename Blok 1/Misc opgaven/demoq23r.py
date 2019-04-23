def main():
    gevonden=False
    while gevonden== False:
        bestandsnaam=input('bestand: ')
        gevonden=leesbestand(bestandsnaam)
def leesbestand(naam):
    try:
        bestand=open('pizza.txt')
        return False
    except FileNotFoundError:
        print('bestand niet gevonden')
main()
