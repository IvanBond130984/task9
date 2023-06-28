print('Введите количество чисел: ')
n=int(input())
lsn=[int(i) for i in input().split()]
if len(lsn)==n:
    st=set(lsn)
    print(len(st))
else:
    print(f'Надо ввести {n} чисел(а)')