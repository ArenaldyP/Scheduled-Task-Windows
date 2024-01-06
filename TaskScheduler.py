import os
import random
from datetime import datetime, timedelta

# Memeriksa apakah tugas jadwal sudah ada
query_exit_code = os.system("schtasks /query /tn SecurityScan > nul 2>&1")
if query_exit_code == 0:
    # Tugas sudah ada, hapus tugas tersebut
    delete_exit_code = os.system("schtasks /delete /f /tn SecurityScan")
    if delete_exit_code == 0:
        print("Tugas 'SecurityScan' berhasil dihapus.")
    else:
        print(f"Gagal menghapus tugas 'SecurityScan'. Kode keluar: {delete_exit_code}")
else:
    print("Tugas 'SecurityScan' tidak ditemukan.")

# Membuat tugas baru
os.system("schtasks /create /tn SecurityScan /tr \"python TaskScheduler.py\" /sc minute /mo 1")

print("Saya sedang melakukan tindakan berbahaya")

filedir = os.path.join(os.getcwd(), "TaskScheduler.py")

maxInterval = 1
interval = 1 + (random.random()) * (maxInterval - 1)
dt = datetime.now() + timedelta(minutes=interval)

t = f"{str(dt.hour).zfill(2)}:{str(dt.minute).zfill(2)}"
d = f"{str(dt.month).zfill(2)}/{str(dt.day).zfill(2)}/{dt.year}"

input()
