import requests
import json

# URL API yang akan diakses
url = "https://jsonplaceholder.typicode.com/posts/1"

# Mengirim permintaan GET ke API
response = requests.get(url)

# Memeriksa apakah permintaan berhasil (kode status 200)
if response.status_code == 200:
    # Mengambil data JSON dari respons
    data = response.json()

    # Mencetak data mentah (tipe dictionary Python)
    print("Data dari API (sebagai dictionary Python):")
    print(data)
    print("-" * 30)

    # Mengakses nilai tertentu dari dictionary
    print("Judul post:", data["title"])
    print("Isi post:", data["body"])

    # Mengubah dictionary kembali ke string JSON yang formatnya rapi
    json_string = json.dumps(data, indent=4)
    print("-" * 30)
    print("Data dalam format JSON yang rapi:")
    print(json_string)

else:
    print(f"Gagal mengambil data. Kode status: {response.status_code}")