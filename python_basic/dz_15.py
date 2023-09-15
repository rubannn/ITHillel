def checknumber(x):
    try:
        nm = int(x)
    except ValueError:
        try:
            nm = float(x)
        except ValueError:
            return x
    return nm


def signum(x):
    return 'від\'ємне' if x < 0 else 'позитивне'


while True:
    n = input("Input number: ")
    if n in ("вихід", "exit", "quit", "e", "q"):
        break
    n = checknumber(n)
    if isinstance(n, float):
        numtype = f'{signum(n)} дробове число'
    elif isinstance(n, int):
        if n == 0:
            numtype = 'нуль'
        else:
            numtype = f'{signum(n)} ціле число'
    else:
        numtype = 'неправильне'
    print(f'Ви ввели {numtype}: {n}')
