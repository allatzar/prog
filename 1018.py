n1 = n2 = n5 = n10 = n20 = n50 = n100 = 0
a = int(input())
while a > 0:
    if a >= 100:
        a = a - 100
        n100 += 1
    elif a >= 50:
        a = a - 50
        n50 += 1
    elif a >= 20:
        a = a - 20
        n20 += 1
    elif a >= 10:
        a = a - 10
        n10 += 1
    elif a >= 5:
        a = a - 5
        n5 += 1
    elif a >= 2:
        a = a - 2
        n2 += 1
    elif a >= 1:
        a = a - 1
        n1 += 1
print(f'{n100} nota(s) de R$ 100,00')
print(f'{n50} nota(s) de R$ 50,00')
print(f'{n20} nota(s) de R$ 20,00')
print(f'{n10} nota(s) de R$ 10,00')
print(f'{n5} nota(s) de R$ 5,00')
print(f'{n2} nota(s) de R$ 2,00')
print(f'{n1} nota(s) de R$ 1,00')
