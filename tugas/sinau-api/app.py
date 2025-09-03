import sys
import datetime as dt
from typing import Dict, Any, Optional
import requests

ALADHAN_BY_CITY = "https://api.aladhan.com/v1/timingsByCity"

# Metode perhitungan (bisa diubah sesuai kebutuhan):
# 2 = University of Islamic Sciences, Karachi (umum dipakai)
# Referensi: https://aladhan.com/prayer-times-api
DEFAULT_METHOD = 5  # ubah jika perlu, mis. 5 (ISNA), 8 (MWL), 3 (Egypt), 4 (Umm Al-Qura)
DEFAULT_SCHOOL = 0  # 0 = Shafi; 1 = Hanafi

def hr():
    return "-" * 48

def format_table(rows: Dict[str, str], title: Optional[str] = None) -> str:
    w = max(len(k) for k in rows) if rows else 0
    lines = []
    if title:
        lines.append(title)
        lines.append(hr())
    for k, v in rows.items():
        lines.append(f"{k.ljust(w)} : {v}")
    return "\n".join(lines)

def fetch_prayer_times_by_city(
    city: str,
    country: str,
    date: Optional[dt.date] = None,
    method: int = DEFAULT_METHOD,
    school: int = DEFAULT_SCHOOL,
) -> Dict[str, Any]:
    if date is None:
        date = dt.date.today()
    date_str = date.strftime("%d-%m-%Y")

    params = {
        "city": city,
        "country": country,
        "method": method,
        "school": school,
        "date": date_str,
    }

    r = requests.get(ALADHAN_BY_CITY, params=params, timeout=15)
    r.raise_for_status()
    data = r.json()
    if data.get("code") != 200:
        raise RuntimeError(f"Gagal dari API AlAdhan: {data}")
    return data["data"]

def show_prayer_table(payload: Dict[str, Any]) -> str:
    timings = payload.get("timings", {})
    date_readable = payload.get("date", {}).get("readable", "")
    meta = payload.get("meta", {})
    tz = meta.get("timezone", "")
    method_info = meta.get("method", {}).get("name", "")

    rows_head = {
        "Tanggal": date_readable,
        "Zona Waktu": tz,
        "Metode": method_info,
    }

    # Pilih yang umum dipakai harian
    wanted = [
        ("Fajr", "Subuh"),
        ("Dhuhr", "Dzuhur"),
        ("Asr", "Ashar"),
        ("Maghrib", "Maghrib"),
        ("Isha", "Isya"),
    ]
    rows_times = {label: timings.get(key, "-") for key, label in wanted}

    return f"""{format_table(rows_head, "Informasi Jadwal Sholat")}
{format_table(rows_times)}"""

def main():
    if len(sys.argv) < 3:
        print("Cara pakai:")
        print("  python app.py \"Purworejo\" \"Indonesia\"")
        print("  python app.py \"Jakarta\" \"Indonesia\"")
        print("Opsional:")
        print("  Tambahkan arg ke-4 dan ke-5 untuk method & school (angka).")
        print("  Contoh: python app.py \"Jakarta\" \"Indonesia\" 2 0")
        sys.exit(0)

    city = sys.argv[1].strip()
    country = sys.argv[2].strip()

    method = DEFAULT_METHOD
    school = DEFAULT_SCHOOL
    if len(sys.argv) >= 4:
        try:
            method = int(sys.argv[3])
        except ValueError:
            pass
    if len(sys.argv) >= 5:
        try:
            school = int(sys.argv[4])
        except ValueError:
            pass

    try:
        data = fetch_prayer_times_by_city(city, country, method=method, school=school)
        print(hr())
        print("JADWAL SHOLAT HARI INI")
        print(hr())
        print(show_prayer_table(data))
        print(hr())
    except requests.Timeout:
        print("[Gagal] Timeout menghubungi API, coba lagi.")
        sys.exit(1)
    except requests.HTTPError as e:
        print(f"[Gagal] HTTP error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[Tak Terduga] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
