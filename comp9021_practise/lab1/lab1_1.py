# Run and study the program named fahrenheit_to_celsius.py (using either v3.5 or v3.6). 
# Then write a program named celsius_to_fahrenheit.py that displays a conversion table from Celsius degrees to Fahrenheit degrees, 
# with the former ranging from 0 to 100 in steps of 10.
min_temperature = 0
max_temperature = 100
step = 10

print('Celsius\tFahrenheit')
for celsius in range(min_temperature, max_temperature + step, step):
    fahrenheit = celsius // 5 * 9 + 32
    print(f'{celsius:7d}\t{fahrenheit:10d}')