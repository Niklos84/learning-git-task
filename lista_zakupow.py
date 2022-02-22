shopping_list = {
    'piekarnia' : ['chleb','bułki','pączek'],
    'warzywniak' : ['marchew','seler','rukola']
}
product_price = [('chleb',4.5),('bułki',0.9),('pączek',2.5),('marchew',3.2),('seler',2.8),('rukola',4.9)]

for i in shopping_list:
    print(f'Idę do {i.capitalize()}, kupuję tu następujące rzeczy: {str(shopping_list[i]).title()}')

count = 0
to_pay = 0

for x,y in shopping_list.items():
    count += len(y)

for x,y in product_price:
    to_pay += y

print(f'W sumie kupuję {count} produktów.')
print(f'W sumie płacę {to_pay} PLN.')