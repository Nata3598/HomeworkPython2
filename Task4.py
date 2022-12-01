# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.



n = int(input('Введите значение N: '))
arr = []
for i in range(-n, n+1):
    arr.append(i)
print(arr)

# получим объект файла
f = open("file.txt", "r")
# считываем все строки
lines = f.readlines()
# закрываем файл
f.close

res = 1

for a in lines :
    i = int(a)
    if i < len(arr):
        print( arr[int(i)], end=' ' )
        res = res * arr[int(i)]
    else:
        print(f"!{i}!", end=' ')

   
print()  
print(f'Результат = {res}')

