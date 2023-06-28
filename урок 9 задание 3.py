st=set()
print('Введите числа: ')
ls=[int(i) for i in input().split()]
for x in ls:
    if x in st:
        print(f'{x} - YES')
    else:
        print(f'{x} - NO')
        st.add(x)