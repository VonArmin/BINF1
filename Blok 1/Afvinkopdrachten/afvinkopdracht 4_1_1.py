while True:
    day=1
    bugs=0
    for day in range(1,6):
        print('day:',day)
        bugsn = int(input('how many bugs have you captured today?: '))
        if bugsn<0:
            print('je kunt geen negatieve bugs vangen!')
        elif bugsn >=0:
            bugs+=bugsn
            day+=1
    if day == 6:
        print ('you have captured',bugs,'over 5 days')

        

        
