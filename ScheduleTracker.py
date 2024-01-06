import os
import pathlib
import subprocess

def CheckValidTask(creator, task):
    # Daftar pembuat tugas terpercaya
    allowlist = ["Microsoft", "Mozilla", "Adobe Systems Incorporated"]
    # Daftar ekstensi file eksekusi yang diizinkan
    extensions = [".exe", ".py", ".dll"]

    # Memeriksa apakah pembuat dan tugas memenuhi kriteria keamanan
    trusted = [creator for x in allowlist if creator.startswith(x)]
    executable = [task for ext in extensions if ext in task]

    if executable:
        exe = task.split(" ")[0]
        p = os.path.expandvars(exe).lower()
        # Memeriksa apakah lokasi file eksekusi berada di dalam direktori system32 Windows
        if p.startswith(r"c:\\windows\\system32") or p.startswith(r"c:\windows\system32"):
            return True
        else:
            return trusted
    else:
        return True

# Mengambil output dari perintah 'schtasks'
output = str(subprocess.check_output(
    "schtasks /query /v /fo csv /nh",
    shell=True)).split("\\r\\n")

# Memisahkan output menjadi baris dan kolom
results = [o.split(",") for o in output]

# Memeriksa setiap tugas yang dihasilkan
for res in results:
    result = [x.strip("\"") for x in res]
    if len(result) > 8:
        name = result[1]
        creator = result[7]
        task = result[8]
        # Memeriksa apakah tugas valid
        if not CheckValidTask(creator, task):
            print(f"{name}, {creator}, {task}")
