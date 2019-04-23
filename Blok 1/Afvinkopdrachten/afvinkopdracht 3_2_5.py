while True:
    veg = input('is there anyone in the party vegetarian? y/n:')
    veg2 = input ('is there anyone in the perty vegan? y/n:')
    glu = input ('is there anyone in the party gluten allergic? y/n:')
    print ('your options are: ')
    if veg == 'y' or veg == 'n' and veg2 == 'y' or veg2 == 'n' and glu == 'y' or glu == 'n' :
        print ("the chef's kitchen")
        print ('corner cafe')
    if veg == 'y' or veg == 'n' and veg2 == 'n' and glu == 'n' :
        print ("mama's fine italian")
    if veg == 'y' or veg == 'n' and veg2 == 'n' and glu == 'y' or glu == 'n' :
        print ('main street pizza company')
    if veg == 'n' and veg2 == 'n' and glu == 'n' :
        print ("joe's gourmet burgers")
  

