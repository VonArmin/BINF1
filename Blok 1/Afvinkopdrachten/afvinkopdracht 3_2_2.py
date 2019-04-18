len1 = int(input('enter the length of area 1: '))
wth1 = int(input('enter the width of area 1: '))

len2 = int(input('enter the length of area2: '))
wth2 = int(input('anter the width of area2: '))

are1 = len1 * wth1
are2 = len2 * wth2
print ('area 1 is',are1 ,'sqft, area 2 is ',are2,'sqft')
if are1 == are2 :
    print ('the areas are the same size')
if are1 > are2 :
    print ('area 1 is bigger than area 2')
if are1 < are2 :
    print ('area 1 is smaller than area 2')
