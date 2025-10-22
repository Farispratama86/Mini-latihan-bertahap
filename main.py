class Dosen:
    def __init__(self, nidn, nama):
        if not (nidn.isdigit() and len(nidn) == 10):
            raise ValueError("NIDN harus terdiri dari 10 digit angka.")
        self.nidn = nidn
        self.nama = nama

    def info(self):
        print(f"Dosen {self.nama} - {self.nidn}")


class Ruang:
    def __init__(self, kode, kapasitas):
        self.kode = kode
        self.kapasitas = kapasitas


class KelasKuliah:
    def __init__(self, kode_kelas, ruang):
        self.kode_kelas = kode_kelas
        self.ruang = ruang
        self.mahasiswa = []

    def tambah_mahasiswa(self, nama):
        if len(self.mahasiswa) < self.ruang.kapasitas:
            self.mahasiswa.append(nama)
        else:
            print(f"\nTidak dapat menambah {nama}. Ruang {self.ruang.kode} sudah penuh!")

    def tampilkan_mahasiswa(self):
        print(f"\nDaftar Mahasiswa di {self.kode_kelas}:")
        for m in self.mahasiswa:
            print(f"- {m}")

    def tampilkan_mahasiswa_awal_DE(self):
        print("\nMahasiswa dengan nama diawali huruf D atau E:")
        for m in self.mahasiswa:
            if m[0].upper() in ['D', 'E']:
                print(f"- {m}")

try:
    dosen1 = Dosen("2301031956", "Triyono")
    dosen2 = Dosen("2301031632", "Faris")
    dosen1.info()
    dosen2.info()
except ValueError as e:
    print(e)

ruangA = Ruang("R101", 29)

kelas = KelasKuliah("TI - 23A5", ruangA)

daftar_mahasiswa = [
    "Adit", "Arsa", "Aziz", "Bima", "Desta", "Dhiwa", "Domingos", "Eka",
    "Fahryan", "Faris", "Fitra", "Gigieh", "Hafan", "Irfan", "Kahfi",
    "Lendra", "Luthfi", "Minan", "Nabil", "Najib", "Nathan", "Pratama",
    "Raka", "Raihan", "Ridho", "Rofi", "Savina", "Trafika", "Viqi"
]

for nama in daftar_mahasiswa:
    kelas.tambah_mahasiswa(nama)

kelas.tampilkan_mahasiswa()
kelas.tampilkan_mahasiswa_awal_DE()
