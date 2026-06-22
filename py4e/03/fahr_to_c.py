inp = input('Enter temperature in fahrenheit: ')

try: 
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except: 
    print('Please enter a Number')