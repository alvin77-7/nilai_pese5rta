from peserta import Peserta
jumlah_peserta = int(input("Jumlah Peserta : "))
daftar_peserta = []

for i in range(jumlah_peserta):
    print(f"\nPeserta ke-{i + 1}")

    nama = input("Nama Peserta : ")
    nilai_tugas = float(input("Nilai Tugas  : "))
    nilai_uts = float(input("Nilai UTS    : "))
    nilai_uas = float(input("Nilai UAS    : "))

    peserta = Peserta(nama,nilai_tugas,nilai_uts,nilai_uas)

    daftar_peserta.append(peserta)

    print("\n=== HASIL PENILAIAN ===")
    peserta.tampilkan_data()
    print(f"Nilai Akhir  : {peserta.hitung_nilai_akhir():.1f}")
    print(f"Grade        : {peserta.hitung_grade()}")
    print(f"Status       : {peserta.cek_kelulusan()}")
