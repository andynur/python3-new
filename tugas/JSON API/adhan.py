import requests

# URL dasar API
BASE_URL = "https://api.aladhan.com/v1/timingsByCity"

# Tanggal statis
DATE = "29-08-2025"

# Negara statis
COUNTRY = "Indonesia"

# Meminta input nama kota dari pengguna
print("-" * 50)
print("APLIKASI JADWAL WAKTU SHOLAT")
print("-" * 50)
city_name = input("Masukkan nama kota di Indonesia (contoh: Jakarta): ")
if (city_name == ""):
  city_name = "Jakarta"

# Membangun URL lengkap dengan parameter dari input pengguna
url = f"{BASE_URL}/{DATE}?city={city_name}&country={COUNTRY}&methd=20"

try:
    # Mengirim permintaan GET ke URL
    response = requests.get(url)
    
    # Memeriksa status respons
    if response.status_code == 200:
        # Mengurai data JSON dari respons
        data = response.json()
        
        # Mengecek apakah ada data jadwal sholat
        if "data" in data and "timings" in data["data"]:
            timings = data["data"]["timings"]
            
            # Mencetak data jadwal sholat dalam bahasa Indonesia
            print("\nJadwal Sholat")
            print(f"Kota    : {city_name.capitalize()}, {COUNTRY.capitalize()}")
            print(f"Tanggal : {data['data']['date']['gregorian']['date']} / {data['data']['date']['hijri']['date']} H")
            print("-" * 50)
            
            # Menampilkan setiap waktu sholat
            print(f"Imsak   : {timings['Imsak']}")
            print(f"Subuh   : {timings['Fajr']}")
            print(f"Terbit  : {timings['Sunrise']}")
            print(f"Dzuhur  : {timings['Dhuhr']}")
            print(f"Ashar   : {timings['Asr']}")
            print(f"Maghrib : {timings['Maghrib']}")
            print(f"Isya    : {timings['Isha']}")
            print("-" * 50)
        else:
            print("Tidak dapat menemukan data jadwal sholat untuk kota tersebut.")
            
    else:
        print(f"Gagal mengambil data. Kode status: {response.status_code}")
        print("Pastikan nama kota yang dimasukkan sudah benar.")

except requests.exceptions.RequestException as e:
    print(f"Terjadi kesalahan saat koneksi ke API: {e}")