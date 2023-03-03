import os
os.system("cls")
from random import randint

data = []
for i in range (10):
    angka = randint(0, 10)
    data.append(angka)

def shellSort(data):
    n = len(data) 
    gap = n // 2 

    while gap > 0: 
        for i in range(gap, n): 
            temp = data[i] 
            j = i 

            while j >= gap and data[j - gap] > temp: 
                data[j] = data[j - gap] 
                j -= gap

            data[j] = temp 
        gap //= 2 

    return data 

print(f"Sebelum: {data}")
hasil = shellSort(data)
print(f"Sesudah: {hasil}")