# --- DATA SIMULASI ---
# Struktur data: Username: {password, saldo, riwayat}
database_users = {
    "ryuza": {"password": "6767", "saldo": 5000000, "riwayat": []}
}

# Variabel global untuk menyimpan user yang sedang login
current_user = None

# --- FUNGSI UTILITAS ---

def format_rupiah(angka):
    """Mengubah angka menjadi format mata uang Rupiah"""
    return f"Rp {angka:,.0f}".replace(",", ".")

def tampilkan_header():
    print("=" * 40)
    print("   DATA KEUANGAN BANK   ")
    print("=" * 40)

# --- LOGIN ---

def login():
    global current_user
    print("\n--- LOGIN ---")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    # Cek apakah user ada di database dan password cocok
    if username in database_users:
        if database_users[username]["password"] == password:
            current_user = username
            print(f"\nLogin Berhasil! Selamat datang, {username}.")
            return True
        else:
            print("Password salah!")
            return False
    else:
        print("Username gak ada ☹️.")
        return False
    
# --- CEK SALDO (READ) ---

def cek_saldo():
    print("\n--- CEK SALDO ---")
    saldo = database_users[current_user]["saldo"]
    print(f"Saldomu sekarang: {format_rupiah(saldo)}")
    input("\nTekan Enter buat balik...")

# --- SETOR TUNAI (UPDATE) ---

def setor_tunai():
    print("\n--- SETOR TUNAI ---")
    try:
        jumlah = int(input("Masukkan jumlah setoran: "))
        if jumlah > 0:
            # Update saldo user
            database_users[current_user]["saldo"] += jumlah
            
            # Catat riwayat
            riwayat = database_users[current_user]["riwayat"]
            riwayat.append(f"Setor: +{jumlah}")
            
            print(f"Berhasil nyetor {format_rupiah(jumlah)}!")
        else:
            print("Jumlah harus lebih dari 0.")
    except ValueError:
        print("Input harus angka!")
    
    input("\nTekan Enter buat balik...")

# --- TARIK TUNAI (DELETE) ---

def tarik_tunai():
    print("\n--- TARIK TUNAI ---")
    saldo = database_users[current_user]["saldo"]
    print(f"Saldomu: {format_rupiah(saldo)}")
    
    try:
        jumlah = int(input("Masukkan jumlah penarikan: "))
        
        if jumlah > 0:
            if jumlah <= saldo:
                # Kurangi saldo
                database_users[current_user]["saldo"] -= jumlah
                
                # Catat riwayat
                riwayat = database_users[current_user]["riwayat"]
                riwayat.append(f"Tarik: -{jumlah}")
                
                print(f"Berhasil narik {format_rupiah(jumlah)}!")
            else:
                print("Saldo gak cukup ☹️")
        else:
            print("Jumlah harus lebih dari 0.")
    except ValueError:
        print("Input harus angka!")
        
    input("\nTekan Enter buat balik...")

# --- RIWAYAT TRANSAKSI (READ) ---

def lihat_riwayat():
    print("\n--- RIWAYAT TRANSAKSI ---")
    riwayat = database_users[current_user]["riwayat"]
    
    if not riwayat:
        print("Belum ada transaksi.")
    else:
        for i, trans in enumerate(riwayat, 1):
            print(f"{i}. {trans}")
            
    input("\nTekan Enter buat balik...")

# --- MENU UTAMA ---

def menu_utama():
    while True:
        tampilkan_header()
        print(f"User: {current_user} | Saldo: {format_rupiah(database_users[current_user]['saldo'])}")
        print("1. Cek Saldo 💰")
        print("2. Setor Tunai 💵")
        print("3. Tarik Tunai 💸")
        print("4. Lihat Riwayat 🕒")
        print("5. Logout 🚪")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            cek_saldo()
        elif pilihan == '2':
            setor_tunai()
        elif pilihan == '3':
            tarik_tunai()
        elif pilihan == '4':
            lihat_riwayat()
        elif pilihan == '5':
            print("Makasih udh mampir 😛.")
            break
        else:
            print("Pilihan gak valid ☹️.")
# --- FUNGSI UTAMA ---

def main():
    while True:
        tampilkan_header()
        print("1. Login")
        print("2. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == '1':
            if login():
                menu_utama()
        elif pilihan == '2':
            print("Program selesai 🎉.")
            break
        else:
            print("Pilihan gak valid ☹️.")
            input("Tekan Enter buat balik...")

if __name__ == "__main__":
    main()