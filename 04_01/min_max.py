countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
population = [17_500_000, 198_000_000, 10_000_000, 30_000_000, 24_000_000, 128_000_000]

def get_pop(pair):
    country, population =pair
    return population


print(min(zip(countries,population), key= get_pop))
print(max(zip(countries,population), key= get_pop))

#we can also define key_function for dictionary, set, list, .... 

