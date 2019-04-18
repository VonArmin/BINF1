def main():
    enzymenseq,enzymen = sequenties()
    analyse(enzymenseq,enzymen)
def sequenties():
    bestand = (open ("enzymen.txt").readlines())
    enzymen=[]
    enzymenseq=[]
    for regel in bestand:
        enzym, enzymseq = regel.split()
        enzymseq=enzymseq.replace ("^","")
        enzymen+=[enzym]
        enzymenseq+=[enzymseq]
    return enzymenseq,enzymen
def analyse(a,b):
    match=0
    dent=0
    knip=0
    seq='ACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCC'
    for x in range(len(a)):
        if a[x] in seq:
            knip=a[x]
            seqw=b[x]
    for x in range(len(a)):
        if match<=0:
            match=seq.find(a[x])
        dent=((match-1)*' ')
    print(seqw,'knipt op positie',match)
    print(seq)
    print(dent,knip)
main()


               
    
    
