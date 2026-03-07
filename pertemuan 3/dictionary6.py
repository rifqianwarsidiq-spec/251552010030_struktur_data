# Membuat dictionary
user = {
    "name": "Fadhli",
    "age": 27
}

# Menambahkan key jika belum ada dengan setdefault
user.setdefault("email", "fadhli@example.com")

# Menghapus key
age = user.pop("age")

# Menampilkan keys dan values
print(user.keys())
print(user.values())

# Menyalin dictionary
user_copy = user.copy()

print(user)
print(user_copy)