print('Введите первый список:')
ls0=[int(i) for i in input().split()]
print('Введите второй список:')
ls1=list(map(int, input().split()))
st0=set(ls0)
st1=set(ls1)
st2=st0.intersection(st1)
print(len(st2))