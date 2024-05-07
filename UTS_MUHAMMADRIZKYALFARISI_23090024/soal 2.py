def kabisat(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    else:
        return False
tahun =int(input("masukan tahun: "))

if kabisat(tahun):
    print(tahun, "ini tahun kabisat")
else:
    print(tahun, "ini bukan tahun kabisat")