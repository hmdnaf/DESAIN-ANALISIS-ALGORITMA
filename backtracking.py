def knapsack_dp(capacity, items):
    n = len(items)
    # Membuat tabel DP (n+1 baris, capacity+1 kolom)
    # Baris merepresentasikan item, Kolom merepresentasikan kapasitas saat ini
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Membangun tabel DP
    for i in range(1, n + 1):
        name, weight, value = items[i-1]
        for w in range(capacity + 1):
            if weight <= w:
                # Pilih maks antara: (nilai item ini + nilai sisa kapasitas) ATAU (nilai tanpa item ini)
                dp[i][w] = max(value + dp[i-1][w-weight], dp[i-1][w])
            else:
                # Item terlalu berat untuk kapasitas w saat ini
                dp[i][w] = dp[i-1][w]

    # Menelusuri kembali (Backtracking) untuk menemukan item mana yang dipilih
    w = capacity
    selected_items = []
    total_weight = 0
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            name, weight, value = items[i-1]
            selected_items.append(items[i-1])
            total_weight += weight
            w -= weight

    return dp[n][capacity], selected_items, total_weight

# --- DATA KASUS (10 ITEM) ---
# Format: (Nama, Berat, Nilai)
items_data = [
    ("Kotak Obat", 2, 95),
    ("Tenda Darurat", 12, 80),
    ("Galon Air", 8, 70),
    ("Karung Beras", 10, 60),
    ("Paket Selimut", 4, 40),
    ("Genset Portable", 15, 85),
    ("Susu Bayi", 3, 55),
    ("Kompor", 2, 30),
    ("Senter", 1, 25),
    ("Radio", 2, 50)
]

max_capacity = 30

# Eksekusi Fungsi
max_value, selected, total_w = knapsack_dp(max_capacity, items_data)

# --- OUTPUT ---
print("=== HASIL IMPLEMENTASI KNAPSACK ===")
print(f"Nilai Profit Maksimum : {max_value}")
print(f"Total Berat           : {total_w} kg")
print("Daftar Item Terpilih  :")
for item in selected:
    print(f"- {item[0]} (Berat: {item[1]}, Nilai: {item[2]})")