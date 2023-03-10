# Post Test 2 Praktikum ASD

##### Nama  : Ayu Cahyarani
##### NIM   : 2209116008
##### Prodi : Sistem Informasi A 22

### Cara Kerja Program

- Membuat algoritma untuk memisahkan tipe datanya
- Untuk elemen yang berada di panjang data dengan tipe int akan langsung di print dengan indeksnya
- Untuk elemen yang berada di panjang data dengan tipe list akan lanjut ke function fiboSearch 
- Di fiboSearch langkah pertama adalah inisialisasi angka fibonacci
- Kemudian mencari nilai dari fibonacci(n) terbesar yang lebih kecil atau sama dengan n
- Menandai indeks awal untuk pencarian
- Melakukan pencarian dengan memeriksa apakah fibo2 lebih besar ke kanan lebih kecil ke kiri
- Jika d dan e lebih besar daripada nilai elemen pada indeks i, lakukan pencarian pada subarray kanan
- Jika d dan e lebih kecil daripada nilai elemen pada indeks i, lakukan pencarian pada subarray kiri
- Jika d dan e ditemukan, kembalikan indeks i
- Jika elemen tidak ditemukan, kembalikan -1

### Fungsionalitas Program

Program ini menggunakan algoritma Fibonacci Search yang berfungsi melakukan pencarian elemen dalam array dengan menggunakan angka fibonacci sebagai titik-titik (indeks) elemen array yang isinya dibandingkan dengan nilai yang dicari. Algoritma ini mengharuskan datanya sudah terurut baik menaik (ascending) maupun menurun (descending). 

### Algoritma

```
import os
os.system("cls")

def fiboSearch(isi, d, e, n) :
    fibo2 = 0
    fibo1 = 1
    fibo = fibo2 + fibo1

    while (fibo < n):
        fibo2 = fibo1
        fibo2 = fibo
        fibo = fibo2 + fibo1
    offset = -1

    while (fibo > 1) :
        i = min(offset + fibo2, n-1)
        if (isi[i] < d and e) :
            fibo = fibo1
            fibo1 = fibo2
            fibo2 = fibo - fibo1
            offset = i
        elif (isi[i] > d and e) :
            fibo = fibo2
            fibo1 = fibo1 - fibo2
            fibo2 = fibo - fibo1
        else :
            return i
        
    if (fibo1 and isi[n-1] == d and e) :
        return n-1
    return -1

def search() :
    for q in range(len(data)):
        if data[q] == a:
            print(f"Arsel di index", q)
        elif data[q] == b:
            print(f"Avivah di index", q)
        elif data[q] == c:
            print(f"Daiva di index", q)
        elif type(data[q]) == list and d and e:
            isi = fiboSearch(data[q], d, "Wahyu", len(data[q]))
            print(f"Wahyu di index", q, "pada kolom", isi)
            isi = fiboSearch(data[q], e, "Wibi", len(data[q]))
            print(f"Wibi di index", q, "pada kolom",  isi)
        else:
            print("Tidak ditemukan")

data = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
a = "Arsel"
b = "Avivah"
c = "Daiva"
d = "Wahyu"
e = "Wibi"

search()
```

### Output

![2209116008 (Ayu Cahyarani) Posttest 2 ASD (fiboSearch1)](https://user-images.githubusercontent.com/121865360/224320373-e9e13ee4-54c6-4cb7-8364-97c5ccab132f.png)

![2209116008 (Ayu Cahyarani) Posttest 2 ASD (fiboSearch2)](https://user-images.githubusercontent.com/121865360/224320445-e0663180-5c53-479b-a1fa-22aa0e783067.png)
