def func(i):
    if i > 5:
        print('100')
    else:
        print('200')

i = 5
for i in range(10):
    i += 2
    if i == 7:
        continue
    print(i)
    
func(i)
print('Цикл закончен')
