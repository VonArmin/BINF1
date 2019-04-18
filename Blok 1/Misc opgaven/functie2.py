def main():
    invoer()

def invoer():
    x=int(input('welk getal wil je vermenigvuldigen?: '))
    y=int(input('met welk getal?: '))
    vermedigvuldig(x,y)

def vermedigvuldig (x=1,y=2):
    print(x*y)

main()
