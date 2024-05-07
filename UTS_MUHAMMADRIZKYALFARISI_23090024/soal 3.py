def hitung_total_harga(daftar_harga):
    total = sum(daftar_harga)
    return total 

def main():
    daftar_harga = [1000, 2000]
    int(input("kopi, susu: "))

    
for i in range(3):
    float(input("1000 ke-{}: ".format(i+1)))

for i in range(3):
    float(input("2000 ke-{}: ".format(i+2)))

total_harga = hitung_total_harga(daftar_harga)
print("total harga dari{kopi, susu,} barang adalah: Rp 3000 {: .2f}".format(jumlah_barang, total_harga))

if __name__ == "__main__":
    main()