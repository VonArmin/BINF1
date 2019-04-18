nummers=[]
total=0
for x in range(20):
    nummer=int(input('voer een nummer in: '))
    nummers.append(nummer)
    total+=nummer
avg=total/20
print(nummers)
print('highest number is:',max(nummers))
print('lowest number is:',min(nummers))
print('total of numbers is:',total)
print('average of numbers is:',avg)



