import requests






# tanggal = input('Masukkan tanggal: ')
tanggal = "28-08-2025"
kota = input('Masukkan nama kota: ')
url = f"https://api.aladhan.com/v1/timingsByCity/{tanggal}?city={kota}&country=Indonesia&method=20"
print(f"Target url: {url}")
response = requests.get(url)   # HTTP GET
data_json = response.json()    # Konversi ke JSON
jadwal_sholat = data_json['data']['timings']
tgl_hijri = data_json['data']['date']['hijri']['date']
print(f"Tgl Hijriah: {tgl_hijri}")
print("Jadwal Sholat:")
print(f"-> Shubuh: {jadwal_sholat['Fajr']}")
print(f"-> Maghrib: {jadwal_sholat['Maghrib']}")