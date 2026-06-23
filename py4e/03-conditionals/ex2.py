print('Enter Hours:')
try: 
    hours  = float(input());
except: 
    print('Please input numeric hours.')
    quit()

print('Enter rate:')
try:
    rate = float(input());
except:
    print('Please input numeric rate')
    quit()


hours = float(hours)
rate = float(rate)
pay = hours * rate

if hours > 40 :
    pay = (40 * rate ) + (hours - 40) * rate * 1.5
else:
    pay = hours * rate

print('\nYour pay will be:')
pay = pay * .85

print(pay)
