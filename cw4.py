fruits=['Apple','Orange','Mango']
vegetables=['pototo','Tomoto','Onion']
beverages=['Water','Juice','Chips']
fruits.append('Grapes')
print(fruits)
vegetables.insert(1,'Garlic')
print(vegetables)
beverages.pop()
print(beverages)
inventory=[fruits,vegetables,beverages]
print(inventory)
print(fruits[:2])
print(vegetables[-1])
length=[len(x) for x in fruits]
print(length)
print('Water' in beverages)
tup=('Apple','pototo','Water')
print(tup)

