def main():
    bestand=open('Documents/Sequenties/Eno1 pseudomonas syringae DNA.fasta')
    Leesbestand(bestand)

def Leesbestand(bestand):
    text=''
    for regel in bestand:
        if not regel.startswith ('>'):
            text+= regel.replace('\n','')
    print(text)
    isDNA(text)

def isDNA(seq):
    dna=True
    for n in seq:
        if n not in 'ATCG':
            dna=False
    if dna==True:
        print('het is dna')
    if dna==False:
        print('het is geen DNA')

main()
