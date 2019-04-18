score = 0
print ('your score =', score)
while True:

    import random

    X = random.randint(0,10)
    Y = random.randint(0,10)
    print ('gegenereerd nummer :', X)

    vraag = input('hoger, lager of gelijk? ')

    if vraag == ('hoger') and X > Y :
        print ('False!')
        score = 0
        print ('your score =', score)
    elif vraag == ('hoger') and X < Y :
        print ('correct!')
        score += 1
        print ('your score =', score)
    elif vraag == ('lager') and X > Y :
        print ('correct!')
        score += 1
        print ('your score =', score)
    elif vraag == ('lager') and X < Y :
        print ('False!')
        score = 0
        print ('your score =', score)
    elif vraag == ('gelijk') and X == Y :
        print ('nice! 5 points!')
        score += 5
        print ('your score =', score)
    elif vraag == ('gelijk') and X != Y :
        print ('false')
        score = 0
        print ('your score =', score)
    else :
        print ('false!')
        score = 0
    
