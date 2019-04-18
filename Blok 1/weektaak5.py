sequence1=open('Documents/Sequenties/Eno1 pseudomonas syringae PROT.txt')
sequence2=open('Documents/Sequenties/Gallus gallus Eno1 Protein.txt')

seq1=[]
seq2=[]
length=0
match=0
nMatch=0

for regel in sequence1:
    if not regel.startswith('>'):
        for letter in regel:
            seq1.append(letter)
for regel in sequence2:
    if not regel.startswith('>'):
        for letter in regel:
            seq2.append(letter)

length1=int(len(seq1))
length2=int(len(seq2))
if length1<length2:
    length=length1
elif length1>=length2:
    length=length2

for x in range(length):
    if seq1[x] == seq2[x]:
        match+=1
    else:
        nMatch+=1

totaal=nMatch+match
percentage=match/nMatch*100

print('totaal:',totaal,'| matching:',match,'| not matching:',nMatch,'| matching percentage:',round(percentage,2),'%')
        
               
                

