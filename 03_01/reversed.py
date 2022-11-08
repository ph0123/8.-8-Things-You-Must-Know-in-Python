countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
x= reversed(countries)
print([i for i in x])
#will print back from Japan to Netherlands.
#we can use another way to do it.
y= countries[::-1]
print([i for i in y])