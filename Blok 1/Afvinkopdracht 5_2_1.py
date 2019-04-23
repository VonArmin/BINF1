def main():
    openfile()
    
def openfile():
    file=open(input('welke file wil je inladen?: '),'r')
    for x in range(5):
        line=file.readline()
        if not line=='':
            print(line)
    file.close() 
main()

