weight=0
mass={'A':71.0788,'R':156.1875,'N':114.1038,'D':115.0887,'C':103.1388,'E':129.1155,
    'Q':128.1307,'G':57.0519,'H':137.1411,'I':113.1594,'L':113.1594,'K':128.1741,
    'M':131.1926,'F':147.1766,'P':97.1167,'S':87.0782,'T':101.1051,'W':186.2132,
    'Y':163.1760,'V':99.1326}
sequence=open ('Documents/Sequenties/Zea mays Eno1 protein.txt')
for regel in sequence:
    if not regel.startswith('>'):
        for letter in regel:
            if letter in mass:
                weight += mass[letter]

print('weight of sequence:',weight)
            
        
        
        
        
        

