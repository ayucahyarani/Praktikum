# Post Test 3 Praktikum ASD

##### Nama  : Ayu Cahyarani
##### NIM   : 2209116008
##### Prodi : Sistem Informasi A 22

### Cara Kerja Program
Membuat objek dari kelas Double
- Membuat class untuk node
- Menginisialisasi untuk kelas node
- Membuat pointer ke node sebelumnya dan selanjutnya
- Membuat class untuk linked list (double list)
- Menginisialisasi untuk kelas double
- Membuat pointer ke node pertama di linked list

Menambahkan beberapa transaksi ke linked list
- Membuat method untuk menambahkan node baru ke linked list
- Jika linked list masih kosong maka node baru akan menjadi head
- Jika tidak maka kunjungi linked list sampai akhir, lalu buat node baru dan tambahkan node baru ke linked list
 
Menampilkan riwayat transaksi pada linked list
- Membuat method untuk menampilkan riwayat transaksi di linked list dengan menampilkan informasi transaksi

Menghapus sebuah transaksi dari linked list
- Membuat method untuk menghapus node dari linked list
- Jika tanggal pada node saat ini cocok dengan tanggal yang dicari
- Jika node saat ini bukan head
- Hapus node saat ini dari linked list
- Jika node saat ini adalah head
- Head diubah menjadi node selanjutnya

### Fungsionalitas Program

Program ini menggunakan algoritma Double Linked List yang merupakan linked list dengan node yang memiliki data dan dua buah reference link (biasanya disebut next dan prev) yang menunjuk ke node sebelum dan node sesudahnya. Lalu mengapa memilih menggunakan algoritma Double Linked List dibandingkan single linked list? Karena double linked list memiliki dua pointer sambungan, yang mana penyisipan bisa dilakukan sebelum data tertentu atau sesudah data tertentu, berbeda dengan single linked list yang hanya memiliki satu pointer sambungan yaitu sambungan kanan(next). 

### Algoritma

```
import os
os.system("cls")

# Class Node
class Node:
    # Inisialisasi node
    def __init__(self, tanggal=None, jumlah=None, deskripsi=None):
        self.prev = None
        self.tanggal = tanggal
        self.jumlah = jumlah
        self.deskripsi = deskripsi
        self.next = None

# Class untuk linked list
class DoubleList:
    # Inisialisasi head
    def __init__(self):
        self.head = None
    
    # Menambah node
    def tambah_transaksi(self, tanggal, jumlah, deskripsi):
        if not self.head:
            self.head = Node(tanggal, jumlah, deskripsi)
        else:
            current = self.head
            while current.next:
                current = current.next
            new_node = Node(tanggal, jumlah, deskripsi)
            current.next = new_node
            new_node.prev = current

    # Menampilkan isi dari list        
    def riwayat_transaksi(self):
        current = self.head
        while current:
            print("\nTanggal   : ", current.tanggal)
            print("Jumlah    : ", current.jumlah)
            print("Deskripsi : ", current.deskripsi)
            print('-'*40)
            current = current.next
            
    # Menghapus node
    def hapus_transaksi(self, tanggal):
        # Membuat pointer yang menunjuk ke node pertama
        current = self.head
        while current:
            if current.tanggal == tanggal:
                if current.prev:
                    current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                else:
                    self.head = current.next
                    if current.next:
                        current.next.prev = None
            current = current.next

# Membuat linked list baru
riwayat_nasabah = DoubleList()

# Menambahkan transaksi ke linked list
riwayat_nasabah.tambah_transaksi("01/01/2023", 5000000, "Setoran pertama")
riwayat_nasabah.tambah_transaksi("02/02/2023", 2000000, "Penarikan tunai")
riwayat_nasabah.tambah_transaksi("17/02/2023", 3000000, "Setoran kedua")

# Mencetak seluruh riwayat transaksi nasabah
print("Menampilkan seluruh riwayat transaksi nasabah:")
riwayat_nasabah.riwayat_transaksi()

# Menghapus salah satu transaksi dari linked list
print("\n\nSetelah transaksi tanggal 01/01/2023 dihapus:")
riwayat_nasabah.hapus_transaksi("01/01/2023")

# Mencetak seluruh riwayat transaksi nasabah setelah salah satu transaksi dihapus
riwayat_nasabah.riwayat_transaksi()
```

### Output

