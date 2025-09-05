# 1: Jadwal Piket harian
piket_hari_ini = ['Udin', 'Udin', 'Udin']

print("Jadwal piket hari ini:")
for nama in piket_hari_ini:
    print("-", nama)

# 2: Rukun Islam
rukun_islam = ('Syahadat', 'Shalat', 'Zakat', 'Puasa', 'Haji')

print("\nDaftar Rukun Islam:")
for rukun in rukun_islam:
    print("-", rukun)


# Tantangan 3: Kitab-Kitab Pelajaran
kitab_pelajaran = {'Kitab Tajwid', 'Kitab Fiqh', 'Kitab Aqidah'}

print("\nKitab-kitab yang dipelajari:")
for kitab in kitab_pelajaran:
    print("-", kitab)


# 4: Biodata Santri
biodata = {
    'nama': 'Udin',
    'kelas': 'X-A',
    'hafalan_juz': 5
}

print("\nBiodata Santri:")
for kunci, nilai in biodata.items():
    print(f"{kunci}: {nilai}")
