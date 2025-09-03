import csv
# panggil module csv diatas dengan import
print("MATERI 10 - FILE HANDLING")
print("-------------------------")
# cari posisi file note.txt dengan raw string (r)
file_path = r"/Users/andynur/Dev/pylearn/materi-10-file/note.txt"
# open() -> buka file target
# mode r -> read only (hanya baca)
file_catatan = open(file_path, "r")
# read() -> baca isi file note.txt
catatan = file_catatan.read()
print(f"Isi Catatan: {catatan}")
# tutup file note.txt
file_catatan.close()


print("---------- OPEN CSV ---------")
anime_file_path = r"/Users/andynur/Dev/pylearn/materi-10-file/anime.csv"
# with ... as -> agar file otomatis ter close 
with open(anime_file_path, "r") as file_anime:
  # gunakan fungsi reader() dari module csv
  baca_file_anime = csv.reader(file_anime)
  # ubah object csv ke list agar bisa di olah
  list_anime = list(baca_file_anime)
  # keluarkan seluruh data dengan for loop
  for anime in list_anime:
    print(anime)    
print('>> proses baca file anime.csv selesai')

# print("---------- ADD CSV ---------")
# anime_baru = [6, "Evan", "Kaijuu no-8", 10.0]
# print(f"Anime baru: {anime_baru}")
# # mode 'a' (append) -> tambah data ke akhir
# with open(anime_file_path, 'a', newline='') as file_anime:
#   # gunakan writer() dari module csv
#   write_anime = csv.writer(file_anime)
#   # fungsi writerow() -> tambah baris baru
#   write_anime.writerow(anime_baru) 
#   print("✅ Anime baru berhasil dicatat!")

# open file -> read (baca) isi
# -> ekstrak data dengan for loop -> olah data (ubah/hapus)
# -> buat ulang seluruh isi baris / file nya
print("---------- OPEN & EKSTRAK CSV ---------")
anime_file_path = r"/Users/andynur/Dev/pylearn/materi-10-file/anime.csv"
data_anime = [] # list kosong
with open(anime_file_path, "r") as file_anime:
  # baca dgn fungsi reader() dari module csv
  baca_file_anime = csv.reader(file_anime)
  # ekstrak tiap baris dengan for loop ke list
  for item_anime in baca_file_anime:
    # .append() -> menambah item ke list
    data_anime.append(item_anime) 

print('>> proses baca & ekstrak selesai')
print(f"data anime dari csv: {data_anime}")
# ubah data per baris index
for item in data_anime:
  if item[1] == "Wildan":
    print("item wildan ditemukan, ubah datanya...")
    item[2] = "Demon Slayer"
    item[3] = 9.5
  else:
    print("skip item, bukan data wildan..")
# hapus data per baris index
del data_anime[5]

print(f"Data anime terkini: {data_anime}")

print("---------- UPDATE CSV ---------")
# mode 'w' (write) -> ubah seluruh baris csv
with open(anime_file_path, 'w', newline='') as file_anime:
  # gunakan writer() dari module csv
  write_anime = csv.writer(file_anime)
  # fungsi writerow() tdk sama dgn writerows()
  # writerow() -> 1 baris
  # writerows() -> seluruh baris
  write_anime.writerows(data_anime) 
  print("✅ Anime terbaru berhasil diubah!")
