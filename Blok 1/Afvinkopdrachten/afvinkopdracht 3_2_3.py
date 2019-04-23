while True:
    number = int(input('which number of pocket would you like to place your bet : '))
    if number == 0:
        print ('the pocket is green ')
    elif number in {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36} :
        print ('the pocket is red')
    elif number in {2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35} :
        print ('the pocket is black')
    else :
        print ('no such pocket')
