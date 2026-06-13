import time 
import winsound

TargetTimeMin = int(input('How many minutes?'))
TargetTimeSec = int(input("How many seconds?"))
TargetTimeTotalInSeconds = (TargetTimeMin*60)+TargetTimeSec
for i in range(TargetTimeTotalInSeconds,-1,-1):
    if TargetTimeSec <1:
        if TargetTimeMin > 0:
            TargetTimeMin -=1
            TargetTimeSec +=60
            TargetTimeSec -= 1
            time.sleep(1)
            print('{:02d}:{:02d}'.format(TargetTimeMin, TargetTimeSec), end = "\r")
    else:
        TargetTimeSec -= 1
        time.sleep(1)
        print('{:02d}:{:02d}'.format(TargetTimeMin, TargetTimeSec), end = "\r")
    if TargetTimeSec < 1 and TargetTimeMin < 1:
        print('\a')
        for i in range(1,10):
            winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
        break
