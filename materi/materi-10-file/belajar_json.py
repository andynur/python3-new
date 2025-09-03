import json
print("---------- READ JSON FILE ---------")
file_json_path = r"/Users/andynur/Dev/belajar-python/materi-10-file/rukun_islam.json"
with open(file_json_path, "r") as file_rukun_islam:
  # baca dengan fungsi load() dari module json
  data_json = json.load(file_rukun_islam)
  print(f"Judul: {data_json['judul']}")
  print(f"Jumlah: {data_json['jumlah']}")
  print(f"Status Kawin: {data_json['status_kawin']}")
  print(f"Status Jomblo: {data_json['status_jomblo']}")
  print(f"Info Hal: {data_json['info']['halaman']}")
  print(f"Info Versi 1: {data_json['info']['riwayat']['versi_1']}")
  for item in data_json['rukun']:
    print(f"-> {item}")

  # akses manual array of object dengan key index
  print(f"Surah ke-1: {data_json['surah'][0]['nama']}")
  # buat garis dengan dikalikan angka
  print("-" * 50)
  print("| No | Nama Surah | Jumlah Ayat | Lokasi Turun |")
  print("-" * 50)
  # tampilkan ke bentuk table garis sederhana
  # keys: no, ayat, nama, turun
  for item_surah in data_json['surah']:
    print(f"| {item_surah['no']} | {item_surah['ayat']} | {item_surah['nama']} | {item_surah['turun']} |")
  print("-" * 50)

print('>> proses baca file json selesai')
