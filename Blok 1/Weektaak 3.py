##open 2 files
##tel het aantal alfabet van de sequentie
##als het totaal gelijk is aand e actg dan is het een dna of rna sequentie.
##      zo niet is het een eiwit.
##print welke sequentie langer/korter is
##print hoeveelheid D E R K in de eiwitsequentie.
var1= open ('Documents/Zea mays Eno1 DNA.fasta', 'r')
var2= open ('Documents/Saccharomyces cerevisiae Eno1 DNA.fasta', 'r')
totaal1=0
totaal2=0
atcg1=0
atcg2=0
d=0
e=0
r=0
k=0
a=0
c=0
t=0
g=0
lading1=0
lading2=0
sequence=var1.read()
length1=len(sequence)
print(length1)
for x in var1 :
    if not x.startswith ('>'):
            A = x.count ('A')
            B = x.count ('B')
            C = x.count ('C')
            D = x.count ('D')
            E = x.count ('E')
            F = x.count ('F')
            G = x.count ('G')
            H = x.count ('H')
            I = x.count ('I')
            J = x.count ('J')
            K = x.count ('K')
            L = x.count ('L')
            M = x.count ('M')
            N = x.count ('N')
            O = x.count ('O')
            P = x.count ('P')
            Q = x.count ('Q')
            R = x.count ('R')
            S = x.count ('S')
            T = x.count ('T')
            U = x.count ('U')
            V = x.count ('V')
            W = x.count ('W')
            X = x.count ('X')
            Y = x.count ('Y')
            Z = x.count ('Z')
            totaal1+=A+B+C+D+E+F+G+H+I+J+K+L+M+N+O+P+Q+R+S+T+U+V+W+X+Y+Z
            atcg1+=A+C+T+G
            d+=D
            e+=E
            r+=R
            k+=K
            a+=A
            c+=C
            t+=T
            g+=G
            lading1=(r+k)-(d+e)
print('************************************************')
if totaal1 == atcg1:
    print ('this is a dna sequence')
    print ('A:',a,'C:',c,'T:',t,'G:',g)
if totaal1 > atcg1:
    print ('this is a protein sequence')
    print ('amount of D:',d,'E:',e)
    print ('amount of R:',r,'K:',k)
    print ('the charge is:',lading1)
print ('the total length of this sequentie is:',totaal1)
print('************************************************') 
d=0
e=0
r=0
k=0
a=0
c=0
t=0
g=0
for x in var2 :
    if not x.startswith ('>'):
            A = x.count ('A')
            B = x.count ('B')
            C = x.count ('C')
            D = x.count ('D')
            E = x.count ('E')
            F = x.count ('F')
            G = x.count ('G')
            H = x.count ('H')
            I = x.count ('I')
            J = x.count ('J')
            K = x.count ('K')
            L = x.count ('L')
            M = x.count ('M')
            N = x.count ('N')
            O = x.count ('O')
            P = x.count ('P')
            Q = x.count ('Q')
            R = x.count ('R')
            S = x.count ('S')
            T = x.count ('T')
            U = x.count ('U')
            V = x.count ('V')
            W = x.count ('W')
            X = x.count ('X')
            Y = x.count ('Y')
            Z = x.count ('Z')
            totaal2+=A+B+C+D+E+F+G+H+I+J+K+L+M+N+O+P+Q+R+S+T+U+V+W+X+Y+Z
            atcg2+=A+T+C+G
            d+=D
            e+=E
            r+=R
            k+=K
            a+=A
            c+=C
            t+=T
            g+=G
            lading2=(r+k)-(d+e)                              
if totaal2 == atcg2:
    print ('this is a dna sequence')
    print ('A:',a,'C:',c,'T:',t,'G:',g)
if totaal2 > atcg2:
    print ('this is a protein sequence')
    print ('amount of D:',d,'E:',e)
    print ('amount of R:',r,'K:',k)
    print ('the charge is:',lading2)
print ('the total length of this sequentie is:',totaal2)
print('************************************************')    
verschil=0
if totaal1 > totaal2:
    print('sequentie 1 is longer than sequentie 2')
    verschil=totaal1-totaal2
    print('difference in length is: ', verschil)
elif totaal1 < totaal2:
    print('sequentie 1 is shorter than sequentie 2')
    verschil=totaal2-totaal1
    print('the differnce in lengte is: ', verschil)

