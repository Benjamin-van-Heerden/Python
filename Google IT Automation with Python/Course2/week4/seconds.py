def to_seconds(hours, minutes, seconds):
    return hours*3600 + minutes*60 + seconds

cont = 'y'
while cont.lower() == 'y':
    try:
        hours = int(input('hours'))
        minutes = int(input('minutes'))
        seconds = int(input('seconds'))
        print('total seconds: ' + str(to_seconds(hours, minutes, seconds)))
    except:
        print('Error')
    cont = input("Try again(y/n)?")
else:
    print('bye')
