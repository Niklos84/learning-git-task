shopping_list = {
    'piekarnia' : ['chleb','bułki','pączek'],
    'warzywniak' : ['marchew','seler','rukola']
}

for i in shopping_list:
    print(f'Idę do {i.capitalize()}, kupuję tu następujące rzeczy: {str(shopping_list[i]).title()}')