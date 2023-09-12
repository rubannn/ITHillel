# За допомогою функції filter() з котрежу слів відфільтрувати
# тільки ті, які є поліндромами (які однаково читаються в
# обидві сторони), регістр літер не враховувати.

def is_palindrom(x):
    return x.lower() ==  x.lower()[::-1]

inputdata = ('Країна', 'шалаш', 'Летел', 'вертольот', 'УЧУ', 'мем', 'мова')

newlist = list(filter(is_palindrom, inputdata))
print(newlist)
