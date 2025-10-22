# Mini Latihan Bertahap – Pemrograman Python

Repository ini menyajikan berbagai latihan dasar dalam bahasa Python yang dibuat untuk keperluan tugas mata kuliah Pemrograman Python, yang dibimbing oleh Bapak Triyono, S.Kom | Program Studi Teknik Informatika – Universitas Duta Bangsa (UDB).

Latihan-latihan ini dikembangkan menggunakan Python dengan konsep Pemrograman Berorientasi Objek (OOP).

## Deskripsi Program

Program terdiri dari tiga kelas utama:

### 1. `Dosen`

Mewakili data seorang dosen.

- Atribut:

  - `nidn` → Nomor Induk Dosen Nasional (harus 10 digit angka)

  - `nama` → Nama dosen

- Validasi:

  - Jika `nidn` bukan angka atau tidak berjumlah 10 digit, maka program akan memunculkan `ValueError`.

- Metode:

  - `info()` → Menampilkan informasi dosen dalam format:

    ```bash
    Dosen [nama] - [nidn]
    ```

### 2. `Ruang`

Mewakili data ruang kelas.

- Atribut:

  - `kode` → Kode ruang (contoh: R101)

  - `kapasitas` → Jumlah maksimum mahasiswa yang dapat ditampung

### 3. `Kelas Kuliah`

Menghubungkan antara ruang kuliah dan mahasiswa.

- Atribut:

  - `kode_kelas` → Kode kelas (contoh: TI - 23A5)

  - `ruang` → Objek dari kelas `Ruang`

  - `mahasiswa` → List untuk menyimpan nama mahasiswa yang terdaftar

- Metode:

  - `tambah_mahasiswa(nama)`

    Menambahkan mahasiswa jika ruang belum penuh.

  - `tampilkan_mahasiswa()`

    Menampilkan seluruh daftar mahasiswa di kelas.

  - `tampilkan_mahasiswa_awal_DE()`

    Menampilkan mahasiswa yang namanya diawali huruf D atau E.

## Alur Program

1. Membuat objek dosen:

   ```bash
   dosen1 = Dosen("2301031956", "Triyono")
   dosen2 = Dosen("23010316321234", "Faris")  # Akan error karena NIDN lebih dari 10 digit
   ```

   Jika NIDN tidak valid, program akan menampilkan pesan kesalahan:

   ```bash
   NIDN harus terdiri dari 10 digit angka.
   ```

2. Membuat objek ruang:

   ```bash
   ruangA = Ruang("R101", 29)
   ```

3. Membuat objek kelas kuliah:

   ```bash
   kelas = KelasKuliah("TI - 23A5", ruangA)
   ```

4. Menambahkan daftar mahasiswa:

   ```bash
   for nama in daftar_mahasiswa:
   kelas.tambah_mahasiswa(nama)
   ```

5. Menampilkan hasil:

- Seluruh mahasiswa di kelas

- Mahasiswa dengan nama diawali huruf D atau E

## Contoh Output

```bash
NIDN harus terdiri dari 10 digit angka.
Dosen Triyono - 2301031956

Daftar Mahasiswa di TI - 23A5:
- Adit
- Arsa
- Aziz
- Bima
- Desta
- Dhiwa
- Domingos
- Eka
- Faris
- Fahryan
- Fitra
- Gigieh
- Hafan
- Irfan
- Kahfi
- Lendra
- Luthfi
- Minan
- Nabil
- Najib
- Nathan
- Pratama
- Raihan
- Raka
- Ridho
- Rofi
- Savina
- Trafika
- Viqi


Mahasiswa dengan nama diawali huruf D atau E:
- Desta
- Dhiwa
- Domingos
- Eka
```

## Konsep yang Digunakan

- Object-Oriented Programming (OOP)

- Validasi Input

- Exception Handling (try-except)

- List dan Perulangan

- Pencarian berdasarkan kondisi huruf awal
