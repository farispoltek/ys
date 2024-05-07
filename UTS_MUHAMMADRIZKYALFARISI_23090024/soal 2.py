def cek_tahun_kabisat(tahun):
    if (tahun % 400 == 0):
        return True
    else:
        return False
    
    int(input("2024,"))

if cek_tahun_kabisat(2024):
    print(2024,"adalah tahun kabisat.")
else:
    print(2024,"bukan tahun kabisat.")