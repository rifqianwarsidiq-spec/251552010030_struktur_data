# Database pengguna
users = {
    "fadhli": "password123",
    "anya": "admin456",
    "abdu": "dev7"
}

# Input dari pengguna
input_username = input("Masukkan username: ")
input_password = input("Masukkan password: ")

# Proses pengecekan login
if input_username in users and users[input_username] == input_password:
    print(f"Login {input_username}: BERHASIL")
else:
    print(f"Login {input_username}: GAGAL - Username atau password salah")