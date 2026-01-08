# Implementasi Algoritma 0/1 Knapsack: Studi Kasus Logistik Drone Bencana Alam

Berisi implementasi penyelesaian masalah 0/1 Knapsack Problem menggunakan pendekatan Dynamic Programming (DP) dengan bahasa pemrograman Python. Proyek ini disusun untuk memenuhi tugas mata kuliah Desain Analisis Algoritma.

### 📌 Deskripsi Kasus
Kasus: Prioritas Muatan Logistik Drone Bencana Alam

Sebuah drone pengantar bantuan memiliki kapasitas angkut terbatas untuk terbang ke desa terpencil yang terisolasi banjir. Sistem harus memilih kombinasi item bantuan dengan total nilai prioritas (urgensi) tertinggi tanpa melebihi kapasitas maksimum drone.

Kapasitas Maksimum Drone: 30 kg

Jumlah Item: 10 jenis barang bantuan

### 📂 Struktur Kode
File utama: backtracking.py

Kode ini menggunakan pendekatan Dynamic Programming untuk membangun tabel solusi optimal secara bottom-up dan melakukan Backtracking (penelusuran balik) pada tabel tersebut untuk mengidentifikasi item mana saja yang terpilih.

Fitur Utama:
Fungsi knapsack_dp: Menghitung nilai profit maksimal.

Tabel DP: Menyimpan keputusan optimal untuk setiap sub-masalah (berat 0 s.d. kapasitas maksimum).

Traceback: Menelusuri item yang diambil untuk ditampilkan ke pengguna.

### 📊 Data Item (10 item)
1. Kotak Obat-obatan Berat: 2 kg Nilai: 95
2. Tenda Darurat Berat: 12 kg Nilai: 80
3. Galon Air Bersih Berat: 8 kg Nilai: 70
4. Karung Beras Berat: 10 kg Nilai: 60
5. Paket Selimut Berat: 4 kg Nilai: 40
6. Genset Portable Berat: 15 kg Nilai: 85
7. Susu Formula Bayi Berat: 3 kg Nilai: 55
8. Kompor Lapangan Berat: 2 kg Nilai: 30
9. Lampu Senter & Baterai Berat: 1 kg Nilai: 25
10. Radio Komunikasi Berat: 2 kg Nilai: 50

### 📝 Hasil Output
Berikut adalah hasil eksekusi program untuk kasus di atas:

Plaintext

=== HASIL IMPLEMENTASI KNAPSACK ===
``` Nilai Profit Maksimum : 375
Total Berat           : 28 kg
Daftar Item Terpilih  :
- Radio (Berat: 2, Nilai: 50)
- Senter (Berat: 1, Nilai: 25)
- Susu Bayi (Berat: 3, Nilai: 55)
- Galon Air (Berat: 8, Nilai: 70)
- Tenda Darurat (Berat: 12, Nilai: 80)
- Kotak Obat (Berat: 2, Nilai: 95)```
  
### 👥 Identitas Kelompok
Nama Anggota 1: [Isi Nama Anda]

Nama Anggota 2: [Isi Nama Teman Anda]

Mata Kuliah: Desain Analisis Algoritma

Tanggal: 4 Januari 2026
