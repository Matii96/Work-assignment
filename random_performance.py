from random import randint

print('wydajnosc = [')
for i in range(0, 10):
    print('    [')
    for j in range(0, 10):

        liczba = randint(10000, 999999) / 10000
        if j < 9:
            print('            %.4f,' % liczba)
        else:
            print('            %.4f' % liczba)
    if i < 9:
        print('    ],')
    else:
        print('    ]')
print(']')
