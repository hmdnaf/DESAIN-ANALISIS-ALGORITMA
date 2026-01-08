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

### 📊 Data Item
