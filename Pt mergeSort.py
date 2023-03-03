import os
os.system("cls")

# mengimport function randint
from random import randint

# merandom 10 bil bulat 0 s/d 10
data = []
for i in range (10):
    angka = randint(0, 10)
    data.append(angka)

def mergerSort(data):
    if len(data) > 1:
        tengah = len(data) // 2
        kiri = data[:tengah]
        kanan = data[tengah:]

        print(f"Kiri: {kiri}")
        print(f"Kanan: {kanan}")
        print(40*"=") 

        # rekursif
        mergerSort(kiri)
        mergerSort(kanan) 

        # penggabungan array
        """
        # a = 0 # indeks untuk array kiri
        # b = 0 # indeks untuk array kanan
        # c = 0 # indeks untuk penggabungannya
        """

        # bisa disingkat dengan
        a = b = c = 0 

        # array kiri dan array kanan masih ada
        while a < len(kiri) and b < len(kanan):
            if kiri[a] < kanan[b]:
                data[c] = kiri[a]
                a += 1
            else :
                data[c] = kanan[b]
                b += 1
            c += 1

        # array kiri masih ada namun array kanan sudah habis
        while a < len(kiri):
            data[c] = kiri[a]
            a += 1
            c += 1

        # array kanan mmasih ada namun array kiri sudah habis
        while b < len(kanan):
            data[c] = kanan[b]
            b += 1
            c += 1

print(f"Sebelum: {data}")
print(40*"=")
mergerSort(data)
print(f"Sesudah: {data}")