doorgaan = 'y'
nummer=0
while doorgaan.lower() =='y':
    print ('mooi man')
    nummer+=1
    print('rondje',nummer)
    doorgaan = input('wil je doorgaan?')
    if doorgaan == 'n':
        print('jammer man!')
