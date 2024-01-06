# Scheduled-Task-Windows
Saat mendapatkan akses ke sistem target, penyerang mungkin tidak memiliki kemampuan untuk melakukannya
langsung mengeksekusi kode berbahaya mereka. Kemampuan mereka mungkin terbatas berdasarkan jenis kerentanan yang telah mereka eksploitasi dan batasan-batasannya ada di atasnya.

Salah satu cara untuk mengatasi keterbatasan ini adalah dengan memanfaatkan penjadwalan tugas. Mendefinisikan tugas terjadwal memungkinkan penyerang tidak hanya mendapatkan kode
eksekusi tetapi juga untuk mempersulit penyelidikan forensik dengan membubarkan rantai serangan. 

Mendapatkan akses awal ke sistem pada satu titik tetapi menjalankan kode hanya pada interval yang tidak ditentukan (atau acak) membuatnya lebih sulit untuk menghubungkannya
dua acara bersama.

## Menjadwalkan Tugas Berbahaya
Sistem operasi Windows menyertakan dukungan untuk penjadwalan tugas melalui
program **schtasks**. Pada sistem Unix, program cron menyediakan fungsi serupa, memungkinkan tugas dijadwalkan untuk dijalankan pada waktu tertentu atau diulang pada waktu yang sama.
interval tertentu
