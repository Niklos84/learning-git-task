shopping_list = {
    'piekarnia' : ['chleb','bułki','pączek'],
    'warzywniak' : ['marchew','seler','rukola']
}

for i in shopping_list:
    print(f'Idę do {i.capitalize()}, kupuję tu następujące rzeczy: {str(shopping_list[i]).title()}')

count = 0

for x,y in shopping_list.items():
    count += len(y)

print(f'W sumie kupuję {count} produktów.')