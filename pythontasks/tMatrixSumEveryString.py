n = int(input("Введите n: "))
m = int(input("Введите m: "))

A = []

for i in range(n):
    list1 = []
    for j in range(m):
        list1.append(int(input("Введите элемент матрицы: ")))
    A.append(list1)

for i in A:
    print(sum(i), end = ' ')