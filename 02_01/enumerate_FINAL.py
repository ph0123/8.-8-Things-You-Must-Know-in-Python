countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
for index in range(len(countries)):
    print(f'{index+1}. {countries[index]}')

'''
Expected output:
1. Netherlands
2. Nigeria
3. Jordan
4. Nepal
5. Niger
6. Japan
'''

'''
Enumerate with for loop
'''
for index, country in enumerate(countries, start=1):
    print(f'{index}. {country}')

'''
A standard for loop
'''
for country in countries:
    print(country)

#easy... not a big problem here.... However, this way is slower than for i in range(len(list)):