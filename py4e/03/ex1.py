print('Enter Hours:')
hours  = input();
print('Enter rate:')
rate = input();

try: 
    hours = float(hours)
    rate = float(rate)
    pay = hours * rate

    if hours > 40 :
        pay = (40 * rate ) + (hours - 40) * rate * 1.5
    else:
        pay = hours * rate

    print('\nYour pay will be:')

    print(pay)
except: 
    print('Please input valid hours and rate.')

