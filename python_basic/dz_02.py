print('=' * 10 + '  I  ' + '=' * 10, True, True)
a_1 = 'qwe'
a_2 = 'qwe'
a1 = a_1
a2 = a_2

print(id(a_1))
print(id(a_2))
print(a1 == a2)
print(a1 is a2)


print('=' * 10 + '  II  ' + '=' * 10, True, False)
b_1 = [12, 5, 'wer']
b_2 = [12, 5, 'wer']

print(id(b_1))
print(id(b_2))
print(b_1 == b_2)
print(b_1 is b_2)


print('=' * 10 + '  III  ' + '=' * 10, True, False, True, True)
a_1 = list(a_1)
a_2 = list(a_2)
print(f'{id(a_1)=}', f'{id(a_2)=}', f'{a_1==a_2=}', f'{a_1 is a_2=}', sep='\n')
print('=' * 20)

b_1 = bool(b_1)
b_2 = bool(b_2)
print(f'{id(b_1)=}', f'{id(b_2)=}', f'{b_1==b_2=}', f'{b_1 is b_2=}', sep='\n')
