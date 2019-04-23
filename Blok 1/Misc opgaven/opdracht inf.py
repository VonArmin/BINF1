score = 0
cont=True
while cont:
    import random
    print('your score =', score)
    X = random.randint(0,100)
    Y = random.randint(0,100)
    antwoord = X+Y
    print ('wat is',X,'+',Y,'?')
    given = int(input('wat is de som van deze 2 getallen? : '))
    if given == antwoord:
        print('NICE! +6')
        score +=6
    elif given != antwoord:
        print('you monkey! score reset.')
        score=0

    
