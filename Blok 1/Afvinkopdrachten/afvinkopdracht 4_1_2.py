time=0
totTime=0
ltime=0
lapn=int(input('how many laps have you driven? '))
for lap in range(lapn):
    lap+=1
    print('track number:',lap)
    timen=int(input('what was the time (in seconds) of this lap? '))
    totTime+=timen
avgTime=totTime/lap
print('total time is: ',totTime)
print('average laptime is: ',round(avgTime,2))
