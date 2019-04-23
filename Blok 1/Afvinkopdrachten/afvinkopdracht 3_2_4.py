msg = 'Did that fix the problem? '
yes = 'nice! ur done'
while True:
    print ('reboot the computer and try to connect.')
    rebootr = input(msg)
    if rebootr == 'yes':
        print (yes)
        break
    if rebootr == 'no':
        print ('reboot the router and try to connect.')
        rebootc = input(msg)
        if rebootc == 'yes':
            print (yes)
            break
        if rebootc == 'no':
            print ('make sure the cables between the router & modem are plugged in firmly')
            cables = input(msg)
            if cables == 'yes':
                print (yes)
                break
            if cables == 'no':
                print ('move the router to an new location and try to connect.')
                location = input(msg)
                if location == 'yes':
                    print (yes)
                    break
                if location == 'no':
                    print ('buy a new router, monkey')
                    break

                
                
            
                
        
