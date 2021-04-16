from pprint import pprint


with open('data.txt', encoding='utf-8') as file:
    lines = file.readlines()
    max_len = len(lines)
    cook_book = {}
    key = lines[0].strip()
    cook_book[key] = []
    keys = ['ingredient_name', 'quantity', 'measure']
    for item in range(max_len):
        str_cook = lines[item].strip()
        if str_cook == (''):
            key = lines[item + 1].strip()
            cook_book[key] = []
        elif not str_cook.isdigit() and str_cook != key:
            values = str_cook.split(' | ')
            names = dict(zip(keys, values))
            cook_book[key] += [names]
    pprint(cook_book)



def get_shop_list_by_dishes(dishes, person_count):
  products = {}
  for dish in dishes:
    ingredients = cook_book[dish]
    for ingredient in ingredients:
      key = ingredient['ingredient_name']
      value = {'quantity': int(ingredient['quantity']) * person_count, 'measure': ingredient['measure']}
      products[key] = value
  pprint(products)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 4)