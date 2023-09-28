class String(str):
    def __init__(self, value):
        self.value = str(value)

    def __add__(self, other):
        if not isinstance(other, String):
            other = String(other)
        return String(super().__add__(other))

    def __sub__(self, other):
        if not isinstance(other, String):
            other = String(other)
        return String(self.value.replace(other, '', 1))


print('     +     ')
s = String('New') + String(890)
print(s, type(s))
s = String('New') + None
print(s, type(s))
s = String('New') + ['s', ' ', 23]
print(s, type(s))
s = String('New') + True
print(s, type(s))


print('     -     ')
s = String('New bala7nce') - 7
print(s, type(s))
s = String(55678345672) - 7
print(s, type(s))
s = String('pineapple apple pine') - 'apple'
print(s, type(s))
s = String('New balance') - 'Bal'
print(s, type(s))
