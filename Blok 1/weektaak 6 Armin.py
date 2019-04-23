import tkinter as tk
import tkinter.filedialog as tkFile
openwindow=tk.Tk()
openwindow.withdraw()

def main():
    choicesMather=SelectOrganisms()
    seq1,seq2=SelectFiles(choicesMather)
    FilterChoice(seq1,seq2,choicesMather)

def SelectOrganisms():
    print('''this program can do the following things:\n
    1. Calculate the GC% of 1 file, can either be an DNA or RNA sequence.
    2. Display wether the sequence is a protein or DNA/RNA.
    3. Display the weight of a protein.
    4. Align 2 protein sequences and check the similarity.\n''')
    choicesMather=int(input('What would you like to do? (number of task):'))      
    return(choicesMather)
def SelectFiles(choice):
    if choice < 4:
        print('Select sequence :')
        seq1=(open(tkFile.askopenfilename(),'r')).readlines()
        seq2=None

        seq1=Cleanfile(seq1)
    elif choice == 4:
        print('Select sequence 1 :')
        seq1=(open(tkFile.askopenfilename(),'r')).readlines()
        print('Select sequence 2 :')
        seq2=(open(tkFile.askopenfilename(),'r')).readlines()

        seq1=Cleanfile(seq1)
        seq2=Cleanfile(seq2)
    else:
        print('\n***************************************************************************\n')
        print('Please choose a number between 1 and 4!')
        print('\n***************************************************************************\n')
        main()
        
    return seq1,seq2

def Cleanfile(seq):
    seqn=''
    for line in seq:
        if not line.startswith('>'):
            for char in line:
                if not char =='\n':
                    seqn+=char                    
    return seqn
            
def FilterChoice(seq1,seq2,choice):
    if choice==1:
        CGtypeFun(seq1,choice)
    if choice==2:
        CGtypeFun(seq1,choice)
    if choice==3:
        WeightFun(seq1)
    if choice==4:
        AlignFun(seq1,seq2)

def CGtypeFun(seq,choice):
    d=0
    e=0
    r=0
    k=0
    a=0
    c=0
    t=0
    g=0
    for letter in seq:
        G = letter.count('G')
        C = letter.count('C')
        A = letter.count('A')
        T = letter.count('T')
        D = letter.count('D')
        E = letter.count('E')
        R = letter.count('R')
        K = letter.count('K')
        d+=D
        e+=E
        r+=R
        k+=K
        a+=A
        c+=C
        g+=G
        t+=T
    totaalgcat = a+t+c+g
    totaalgc = g+c
    aandeel = totaalgc / totaalgcat * 100
    if len(seq)==totaalgcat:
        seqtype='RNA/DNA'
    if len(seq)>totaalgcat:
        seqtype='PROTEIN'
    print('\n***************************************************************************\n')
    if choice ==1:
        print ('The amount of CG nucleotides in the sequence is :', totaalgc)
        print ('Total amount of nucleotides in the sequence is  :', len(seq))
        print ('The % of CG in the sequence is                  :', round( aandeel,2), '%')
    if choice ==2:
        print ('Total amount of nucleotides in sequence is       :',len(seq))
        print ('Total amount of ATCG in the sequence is          :',totaalgcat)
        print ('Type of the chosen sequence is                   :',seqtype)
        if seqtype=='RNA/DNA':
            print ('A:',a,'C:',c,'T:',t,'G:',g)
        if seqtype=='PROTEIN':
            print ('Amount of D:',d,'E:',e)
            print ('Amount of R:',r,'K:',k)
            print ('The charge is:',(r+k)-(d+e))
    print('\n***************************************************************************\n')
    main()
                   
def WeightFun(seq):
    weight=0
    mass={'A':71.0788,'R':156.1875,'N':114.1038,'D':115.0887,'C':103.1388,'E':129.1155,
    'Q':128.1307,'G':57.0519,'H':137.1411,'I':113.1594,'L':113.1594,'K':128.1741,
    'M':131.1926,'F':147.1766,'P':97.1167,'S':87.0782,'T':101.1051,'W':186.2132,
    'Y':163.1760,'V':99.1326}
    for regel in seq:
        for letter in regel:
            if letter in mass:
                weight += mass[letter]
    lenprot=len(seq)
    weight-=(lenprot-1)*18.0154
    print('\n***************************************************************************\n')
    print('Length of the sequence is :',len(seq))
    print('Weight of the sequence is :',round(weight,2))
    print('\n***************************************************************************\n')
    main()
    
def AlignFun(seq1,seq2):
    lseq1=[]
    lseq2=[]
    length=0
    match=0
    nMatch=0
    for letter in seq1:
        lseq1.append(letter)
    for letter in seq2:
        lseq2.append(letter)


    if len(seq1)<len(seq2):
        length=len(seq1)
    else:
        length=len(seq2)

    for x in range(length):
        if seq1[x] == seq2[x]:
            match+=1
        else:
            nMatch+=1


    totaal=nMatch+match
    percentage=match/totaal*100

    print('\n***************************************************************************\n')
    print('total:',totaal,'| matching:',match,'| not matching:',nMatch,'| matching percentage:',round(percentage,2),'%')
    print('\n***************************************************************************\n')
    main()

main()

