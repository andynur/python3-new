import requests

# URL dasar API
BASE_URL = "https://api.aladhan.com/v1/timingsByCity"

# Tanggal statis
DATE = "28-08-2025"

# Negara statis
COUNTRY = "Indonesia"

# Meminta input nama kota dari pengguna
city_name = input("Masukkan nama kota di Indonesia (contoh: Jakarta): ")

# Membangun URL lengkap dengan parameter dari input pengguna
url = f"{BASE_URL}/{DATE}?city={city_name}&country={COUNTRY}&method=8"

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
            print("\nJadwal Sholat:")
            print(f"Untuk Kota: {city_name.capitalize()}, {COUNTRY.capitalize()}")
            print(f"Pada Tanggal: {data['data']['date']['readable']}")
            print("-" * 30)
            
            # Menampilkan setiap waktu sholat
            print(f"Imsak:    {timings['Imsak']}")
            print(f"Subuh:    {timings['Fajr']}")
            print(f"Terbit:   {timings['Sunrise']}")
            print(f"Dzuhur:   {timings['Dhuhr']}")
            print(f"Ashar:    {timings['Asr']}")
            print(f"Maghrib:  {timings['Maghrib']}")
            print(f"Isya:     {timings['Isha']}")
            
        else:
            print("Tidak dapat menemukan data jadwal sholat untuk kota tersebut.")
            
    else:
        print(f"Gagal mengambil data. Kode status: {response.status_code}")
        print("Pastikan nama kota yang dimasukkan sudah benar.")

except requests.exceptions.RequestException as e:
    print(f"Terjadi kesalahan saat koneksi ke API: {e}")