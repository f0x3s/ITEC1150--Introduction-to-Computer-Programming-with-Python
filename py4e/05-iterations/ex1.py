total = 0
count = 0

while True:
    print('Input number')
    number = input()

    if (number == 'done'):
        break

    try:
        number = float(number)
        total = total + number
        count = count + 1
    except:
        print('Error: expecting numeric input or "done"')

if count != 0:
    average = total/count
else:
    average = 0

print('total: ', total)
print('average: ', average)
print('count: ', count)
        
