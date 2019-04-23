stop=1
while True:
    factorial=int(input('what factorial would you like to calculate?: '))

    if factorial>=10000:
        print('the number is too damn high!')
    if factorial<10000:
        for nummer in range(factorial):
            if nummer>0:
                factorial*=stop
                stop+=1
        print(factorial)
        stop=1
    

