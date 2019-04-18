sequence1=open('Documents/Sequenties/temp/AAQ96629.1.fasta')
sequence2=open('Documents/Sequenties/temp/ACS44348.1.fasta')

seq1=[]
seq2=[]
length=0
match=0
nMatch=0
for regel in sequence1:
    if not regel.startswith('>'):
        for letter in regel:
            if not letter == '\n':
                seq1.append(letter)
            

for regel in sequence2:
    if not regel.startswith('>'):
        for letter in regel:
            if not letter =='\n':
                seq2.append(letter)
#de sequentie wordt in een lijst gezet dit is handig om later naar te refereren

length1=int(len(seq1))
length2=int(len(seq2))
if length1<length2:
    length=length1
elif length1>=length2:
    length=length2
#de lengtes worden vergeleken, zodat het script niet vast loopt als de langste eerst is.

for x in range(length):
    if seq1[x] == seq2[x]:
        match+=1
    else:
        nMatch+=1

#het script loopt door tot de kortste sequentie, match en not match worden bijgehouden.

totaal=nMatch+match
percentage=match/totaal*100

print('totaal:',totaal,'| matching:',match,'| not matching:',nMatch,'| matching percentage:',round(percentage,2),'%')
        
               
                

