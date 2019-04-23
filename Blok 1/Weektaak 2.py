print ('\n')
print('this program will list the percentage CG and total amount of CG in the sequence')
while True :
    sequence1 = input ('''Saved organisms for Eno1 :

    PS - Pseunomas Syringae
    MM - Mus Musculus
    GG - Gallus GAllus
    SC - Saccharomyces cerevisiae
    ZM - Zea Mays

Type the code of the organism you would like to analyze :''')

    sequence2 = input ('''types of sequences saved :

    DNA
    RNA

Which type of sequence would you like to analyze? :''')
    print ('\n')
#sequence 1 en sequence 2 worden gecombineerd tot 1 sequence, sequence 3.
    sequence3 = sequence1 + sequence2
#PS is none wanneer er geen goede combinatie ingevoerd is.
#als de invoer overeenkomt met een gedefinieerde sequence wordt het overeenkomende bestand geladen.
    while True :
        if sequence3 == 'PSDNA' :                       
            PS = open ("Documents/Eno1 pseudomonas syringae DNA.fasta", "r")
        elif sequence3 == 'PSRNA' :
            PS = open ("Documents/Eno1 pseudomonas syringae RNA.txt", "r")
        elif sequence3 == 'MMDNA' :
            PS = open ("Documents/eno1 Mus musculus DNA.fasta", "r")
        elif sequence3 == 'MMRNA' :
            PS = open ("Documents/eno1 Mus musculus RNA.txt", "r")
        elif sequence3 == 'GGDNA' :
            PS = open ("Documents/Gallus gallus Eno1 DNA.fasta", "r")
        elif sequence3 == 'GGRNA' :
            PS = open ("Documents/Gallus gallus Eno1 RNA.txt", "r")
        elif sequence3 == 'SCDNA' :
            PS = open ("Documents/Saccharomyces cerevisiae Eno1 DNA.fasta", "r")
        elif sequence3 == 'SCRNA' :
            PS = open ("Documents/Saccharomyces cerevisiae Eno1 RNA.txt", "r")
        elif sequence3 == 'ZMDNA' :
            PS = open ("Documents/Zea mays Eno1 DNA.fasta", "r")
        elif sequence3 == 'ZMRNA' :
            PS = open ("Documents/Zea mays Eno1 RNA.txt", "r")
        else :
            PS = None
            
#als er geen goede combinatie ingevoerd is stopt de loop en begint bij de PS
                
        aandeel =0
        percentage =0
        totaal =0       
        if PS != None :
            for x in PS :
                if not x.startswith('>'):
                    G = x.count('G')
                    C = x.count('C')
                    A = x.count('A')
                    T = x.count('T')
                    

                    totaal += G+C+A+T   #berekend totaal aantal GCAT

                    percentage += G+C   #berekend hoveelheid GC

                    aandeel = percentage / totaal * 100   #berekend percentage GC

        print ('**************************************************************')
#informatie venster, wanneer PS none is wordt er geen data maar een foutmelding weergeven.
        
        if sequence1 == 'PS' :
            print ('chosen organism : "Pseudomonas Syringae"')
        if sequence1 == 'MM' :
            print ('chosen organism : "Mus Musculus"')
        if sequence1 == 'GG' :
            print ('chosen organism : "Gallus Gallus"')
        if sequence1 == 'SC' :
            print ('chosen organism : "Sacchasrmyces Cervisiae"')
        if sequence1 == 'ZM' :
            print ('chosen organism : "Zae Mays"')
        if sequence2 == 'DNA' :
            print ('chosen type of sequence is : DNA')
        if sequence2 == 'RNA' :
            print ('chosen type of sequence : RNA')
        if PS == None :
            print ('No valid combination selected!')
        if PS != None :
            print ('the amount of CG nucleotides in the sequence is :', percentage)    #print hoveelheid CG nucleotides
            print ('total amount of nucleotides in sequnce is       :', totaal)
            print ('the % of CG in the sequence is                  :', round( aandeel,2), '%') #print afgeronde % GC
        print ('**************************************************************')
        print ('\n')
        break
