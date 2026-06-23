print('Please input sccore between 0 and 1: ')
try:
    score = float(input())
except:
    print('Please input numeric score.')
    quit()

if score >= 0.9 :
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
else:
    print('F')
