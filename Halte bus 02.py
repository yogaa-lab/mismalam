"""
SISTEM HALTE BUS - INTERAKTIF (enqueue & dequeue)
====================================================
Semua data (halte, rute, jadwal, penumpang) diisi sendiri
oleh pengguna lewat menu, tidak ada data contoh bawaan.
"""

from collections import deque

# ===== PENYIMPANAN DATA (awalnya kosong, diisi lewat menu) =====
antrian_halte = {}   # nama_halte -> deque(penumpang)
rute_bus = {}        # nama_rute  -> [list nama halte]
jadwal_rute = {}     # nama_rute  -> deque(jam keberangkatan)


# ===== FUNGSI DASAR ENQUEUE / DEQUEUE =====

def enqueue(antrian, data):
    """Memasukkan data ke belakang antrian."""
    antrian.append(data)


def dequeue(antrian):
    """Mengeluarkan data dari depan antrian. Mengembalikan None jika kosong."""
    if antrian:
        return antrian.popleft()
    return None


# ===== FUNGSI HALTE =====

def tambah_halte():
    nama = input("Nama halte baru: ").strip()
    if nama in antrian_halte:
        print(f"Halte '{nama}' sudah ada.")
        return
    antrian_halte[nama] = deque()
    print(f"Halte '{nama}' berhasil ditambahkan.")


def tampilkan_halte():
    if not antrian_halte:
        print("Belum ada halte.")
        return
    print("Daftar halte:", ", ".join(antrian_halte.keys()))


def tambah_penumpang():
    if not antrian_halte:
        print("Belum ada halte. Tambahkan halte dulu.")
        return
    nama_halte = input("Nama halte: ").strip()
    if nama_halte not in antrian_halte:
        print(f"Halte '{nama_halte}' tidak ditemukan.")
        return
    nama_penumpang = input("Nama penumpang: ").strip()
    enqueue(antrian_halte[nama_halte], nama_penumpang)
    print(f"{nama_penumpang} mengantri di {nama_halte}.")


def bus_datang():
    if not antrian_halte:
        print("Belum ada halte.")
        return
    nama_halte = input("Nama halte: ").strip()
    if nama_halte not in antrian_halte:
        print(f"Halte '{nama_halte}' tidak ditemukan.")
        return
    try:
        kapasitas = int(input("Kapasitas bus: ").strip())
    except ValueError:
        print("Kapasitas harus berupa angka.")
        return

    naik = []
    for _ in range(kapasitas):
        penumpang = dequeue(antrian_halte[nama_halte])
        if penumpang is None:
            break
        naik.append(penumpang)

    if naik:
        print(f"Bus di {nama_halte} menaikkan: {', '.join(naik)}")
    else:
        print(f"Tidak ada penumpang di {nama_halte}.")


def tampilkan_antrian_halte():
    if not antrian_halte:
        print("Belum ada halte.")
        return
    nama_halte = input("Nama halte: ").strip()
    if nama_halte not in antrian_halte:
        print(f"Halte '{nama_halte}' tidak ditemukan.")
        return
    antrian = antrian_halte[nama_halte]
    print(f"Antrian {nama_halte}: {list(antrian) if antrian else 'kosong'}")


# ===== FUNGSI RUTE & JADWAL =====

def tambah_rute():
    nama_rute = input("Nama rute baru: ").strip()
    if nama_rute in rute_bus:
        print(f"Rute '{nama_rute}' sudah ada.")
        return

    urutan = input("Urutan halte yang dilewati (pisahkan koma, contoh: Halte A,Halte B): ").strip()
    daftar_halte = [h.strip() for h in urutan.split(",") if h.strip()]

    for h in daftar_halte:
        if h not in antrian_halte:
            print(f"Halte '{h}' belum terdaftar. Tambahkan halte itu dulu.")
            return

    jadwal_input = input("Jadwal keberangkatan (pisahkan koma, contoh: 06:00,07:00): ").strip()
    daftar_jadwal = [j.strip() for j in jadwal_input.split(",") if j.strip()]

    rute_bus[nama_rute] = daftar_halte
    jadwal_rute[nama_rute] = deque(daftar_jadwal)
    print(f"Rute '{nama_rute}' berhasil ditambahkan.")


def tampilkan_rute():
    if not rute_bus:
        print("Belum ada rute.")
        return
    nama_rute = input("Nama rute: ").strip()
    if nama_rute not in rute_bus:
        print(f"Rute '{nama_rute}' tidak ditemukan.")
        return
    print(f"{nama_rute}: {' -> '.join(rute_bus[nama_rute])}")


def tampilkan_semua_rute():
    if not rute_bus:
        print("Belum ada rute.")
        return
    for nama_rute, daftar_halte in rute_bus.items():
        print(f"{nama_rute}: {' -> '.join(daftar_halte)}")


def tampilkan_jadwal():
    if not jadwal_rute:
        print("Belum ada rute.")
        return
    nama_rute = input("Nama rute: ").strip()
    if nama_rute not in jadwal_rute:
        print(f"Rute '{nama_rute}' tidak ditemukan.")
        return
    jadwal = jadwal_rute[nama_rute]
    print(f"Jadwal {nama_rute}: {list(jadwal) if jadwal else 'tidak ada lagi'}")


def bus_berangkat():
    if not jadwal_rute:
        print("Belum ada rute.")
        return
    nama_rute = input("Nama rute: ").strip()
    if nama_rute not in jadwal_rute:
        print(f"Rute '{nama_rute}' tidak ditemukan.")
        return
    jam = dequeue(jadwal_rute[nama_rute])
    if jam:
        print(f"Bus {nama_rute} berangkat pukul {jam}.")
    else:
        print(f"Tidak ada lagi bus untuk {nama_rute} hari ini.")


# ===== MENU UTAMA =====

def cetak_menu():
    print("\n===== SISTEM HALTE BUS =====")
    print("1. Tambah Halte")
    print("2. Tampilkan Daftar Halte")
    print("3. Tambah Penumpang ke Halte")
    print("4. Bus Datang (naikkan penumpang)")
    print("5. Tampilkan Antrian di Halte")
    print("6. Tambah Rute + Jadwal")
    print("7. Tampilkan Satu Rute")
    print("8. Tampilkan Semua Rute")
    print("9. Tampilkan Jadwal Rute")
    print("10. Bus Berangkat (sesuai jadwal)")
    print("0. Keluar")


def main():
    while True:
        cetak_menu()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tambah_halte()
        elif pilihan == "2":
            tampilkan_halte()
        elif pilihan == "3":
            tambah_penumpang()
        elif pilihan == "4":
            bus_datang()
        elif pilihan == "5":
            tampilkan_antrian_halte()
        elif pilihan == "6":
            tambah_rute()
        elif pilihan == "7":
            tampilkan_rute()
        elif pilihan == "8":
            tampilkan_semua_rute()
        elif pilihan == "9":
            tampilkan_jadwal()
        elif pilihan == "10":
            bus_berangkat()
        elif pilihan == "0":
            print("Terima kasih telah menggunakan Sistem Halte Bus.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


if __name__ == "__main__":
    main()