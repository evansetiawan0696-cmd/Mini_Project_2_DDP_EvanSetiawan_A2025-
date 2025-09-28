print("-" * 20)
print("nama : Evan_Setiawan")
print("NIM : 2509116036")
print("Kelas : Sisfor A 2025")
print("tugas : minpro 1")
print("-" * 20)

print()
print()

# Sistem pendaftaran pasien pada Klinik UNMUL
print("=" * 30)
print("selamat datang di Klinik UNMUL")
print("=" * 30)

#dictionary data pengguna
data_pasien = []
data_pendaftaran = {}

# data dictionary untuk login admin
admin_user = {
    "admin": {"password": "admin123", "role": "admin"}
}

# Dictionary untuk login pasien
pasien_user = {
    "pasien": {"password": "pasien123", "role": "pasien"}
}

# Fungsi login
def login():
    while True:
        try:
            username = input("Masukkan username: ")
            if username.lower() == 'keluar':
                return
            if not username:
                raise ValueError("Username tidak boleh kosong.")
            password = input("Masukkan password: ")
            if not password:
                raise ValueError("Password tidak boleh kosong.")
            if username in admin_user and admin_user[username]["password"] == password:
                print("Login berhasil!")
                return admin_user[username]["role"]
            elif username in pasien_user and pasien_user[username]["password"] == password:
                print("Login berhasil!")
                return pasien_user[username]["role"]
            else:
                print("Username atau password salah. Coba lagi.")
        except ValueError as e:
            print(f"Error: {e} Coba lagi.")
            print("Login gagal.")
            return

# Login sebelum masuk ke program utama
print("Silakan login terlebih dahulu.")
role = login()

if role == "admin":
    def admin_menu():
        global data_pasien
        while True:
            try:
                print("\n=== Menu Admin ===")
                print("1. Create Pasien")
                print("2. Read Pasien")
                print("3. Update Pasien")
                print("4. Delete Pasien")
                print("5. Keluar")
                pilihan_menu = input("Pilih (1-5): ")
                if pilihan_menu == "1":
                    nama = input("masukkan nama : ")
                    umur = input("berapa umur anda: ")
                    gender = input("jenis kelamin: ")
                    alamat = input("alamat : ")
                    TTL = input("tempat, tanggal lahir: ")
                    pasien = {
                        'id': (data_pasien) + 1,
                        'nama': nama,
                        'umur': umur,
                        'gender': gender,
                        'alamat': alamat,
                        'TTL': TTL
                    }
                    data_pasien.append(pasien)
                    print("Data pasien berhasil disimpan dengan ID:", pasien['id'])
                elif pilihan_menu == "2":
                    if not data_pasien:
                        print("Tidak ada data pasien.")
                    else:
                        print("\nDaftar Pasien:")
                        for p in data_pasien:
                            print("- ID: {}, Nama: {}, Umur: {}, Gender: {}, Alamat: {}, TTL: {}".format(p['id'], p['nama'], p['umur'], p['gender'], p['alamat'], p['TTL']))
                elif pilihan_menu == "3":
                    if not data_pasien:
                        print("Tidak ada data pasien.")
                    else:
                        try:
                            pid = int(input("Masukkan ID pasien: "))
                        except ValueError:
                            print("ID harus berupa angka.")
                            continue
                        found = False
                        for p in data_pasien:
                            if p['id'] == pid:
                                nama = input("Nama baru (enter untuk tetap): ") or p['nama']
                                umur = input("Umur baru (enter untuk tetap): ") or p['umur']
                                gender = input("Gender baru (enter untuk tetap): ") or p['gender']
                                alamat = input("Alamat baru (enter untuk tetap): ") or p['alamat']
                                TTL = input("TTL baru (enter untuk tetap): ") or p['TTL']
                                p['nama'] = nama
                                p['umur'] = umur
                                p['gender'] = gender
                                p['alamat'] = alamat
                                p['TTL'] = TTL
                                print("Data berhasil diupdate.")
                                ditemukan = True
                                break
                        if not ditemukan:
                            print("Pasien tidak ditemukan.")
                elif pilihan_menu == "4":
                    if not data_pasien:
                        print("Tidak ada data pasien.")
                    else:
                        try:
                            pid = int(input("Masukkan ID pasien untuk dihapus: "))
                        except ValueError:
                            print("ID harus berupa angka.")
                            continue
                        data_pasien = [p for p in data_pasien if p['id'] != pid]
                        print("Pasien berhasil dihapus.")
                elif pilihan_menu == "5":
                    break
                else:
                    print("Pilihan tidak valid.")
            except Exception as e:
                print(f"Error: {e}. Coba lagi.")
    admin_menu()
else:
    def pasien_menu():
        global data_pasien
        while True:
            print("\n=== Menu Pasien ===")
            print("1. Daftar sebagai pasien baru")
            print("2. Daftar sebagai pasien lama")
            print("3. Keluar")
            pilihan_menu = input("Pilih (1-3): ")
            
            if pilihan_menu == "1":
                print("silahkan mendaftarkan data diri anda dahulu")
                # Input data pasien
                nama = input("masukkan nama : ")
                umur = input("berapa umur anda: ")
                gender = input("jenis kelamin: ")
                alamat = input("alamat : ")
                TTL = input("tempat, tanggal lahir: ")
                
                print("data pasien: nama={}, umur={}, gender={}, alamat={}, TTL={}".format(nama, umur, gender, alamat, TTL))
                
                # Read Validasi data
                while True:
                    print("-" * 20)
                    apakah_data_valid = input("Apakah data sudah benar? (iya/tidak): ")
                    
                    if apakah_data_valid == "iya":
                        patient = {
                            'id': len(data_pasien) + 1,
                            'nama': nama,
                            'umur': umur,
                            'gender': gender,
                            'alamat': alamat,
                            'TTL': TTL
                        }
                        data_pasien.append(patient)
                        print("data berhasil disimpan dengan ID:", patient['id'])
                        break
                    elif apakah_data_valid == "tidak":
                        print("Silakan isi ulang data Anda.")
                        # Input ulang data
                        nama = input("masukkan nama : ")
                        umur = input("berapa umur anda: ")
                        gender = input("jenis kelamin: ")
                        alamat = input("alamat : ")
                        TTL = input("tempat, tanggal lahir: ")
                        
                        print("data pasien: nama={}, umur={}, gender={}, alamat={}, TTL={}".format(nama, umur, gender, alamat, TTL))
                    else:
                        print("Pilihan tidak valid. Silakan pilih 'iya' atau 'tidak'.")
                
                # Pemilihan poli dan keluhan
                print("silahkan memilih poli: ")
                print()
                PILIHAN_POLI = ("poli umum", "poli lansia", "poli anak", "poli gigi")
                print("-" * 40)
                print(PILIHAN_POLI)
                print("-" * 40)
                print()
                
                pilihan_poli = input("pilih poli: ")
                keluhan = input("keluhan yang anda rasakan: ")
                
                # Rincian pendaftaran
                print("=" * 40)
                print("rincian pendaftaran")
                print("=" * 40)
                print()
                print("-" * 40)
                print("status: pasien baru")
                print("pilihan poli:", pilihan_poli)
                print("keluhan:", keluhan)
                print("-" * 40)
                print()
                print("silahkan menunggu panggilan, terimakasih")
                print("terimakasih, lekas sembuh")
                
                # Konfirmasi ingin berobat lagi
                print("-" * 40)
                berobat_lagi = input("Apakah anda ingin berobat lagi? (iya/tidak): ")
                if berobat_lagi == "tidak":
                    print("=" * 40)
                    print("Terima kasih telah menggunakan layanan Klinik UNMUL.")
                    print("=" * 40)
                    return 
                print()
            
            elif pilihan_menu == "2":
                print("-" * 40)
                print()
                print("status : pasien lama")
                print()
                
                # Pemilihan poli dan keluhan
                print("silahkan memilih poli: ")
                print()
                PILIHAN_POLI = ("poli umum", "poli lansia", "poli anak", "poli gigi")
                print("-" * 40)
                print(PILIHAN_POLI)
                print("-" * 40)
                print()
                
                pilihan_poli = input("pilih poli: ")
                keluhan = input("keluhan yang anda rasakan: ")
                
                # Rincian pendaftaran
                print("=" * 40)
                print("rincian pendaftaran")
                print("=" * 40)
                print()
                print("-" * 40)
                print("status: pasien lama")
                print("pilihan poli:", pilihan_poli)
                print("keluhan:", keluhan)
                print("-" * 40)
                print()
                print("silahkan menunggu panggilan, terimakasih")
                print("terimakasih, lekas sembuh")
                
                # Konfirmasi ingin berobat lagi
                print("-" * 40)
                berobat_lagi = input("Apakah anda ingin berobat lagi? (iya/tidak): ")
                if berobat_lagi == "tidak":
                    print("=" * 40)
                    print("Terima kasih telah menggunakan layanan Klinik UNMUL.")
                    print("=" * 40)
                    return 
                print()
            
            elif pilihan_menu == "3":
                print("=" * 40)
                print("Terima kasih telah menggunakan layanan Klinik UNMUL.")
                print("=" * 40)
                break
            else:
                print("Pilihan tidak valid.")
    
    pasien_menu()
