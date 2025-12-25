print ("Tugas UAS Akhir") 


print("PT. SAMPLE INDONESIA")
print("Jl. Jend Sudirman No.43")
print("Jakarta Utara 14330")
print("Telp. (021) 669 6666")
print("Fax.  (021) 6669 5566\n")

print("========== FAKTUR TAGIHAN ==========\n")

print("No Faktur : 00000456\n")

print("Pembeli : SAMPLE INDONESIA, PT.")
print("Nama    : Mr. Dimas Prasetyo")
print("Alamat  : DEUTSCHE BANK BUILDING LEVEL 15B SUITE 50")
print("          JL. IMAM BONJOL NO.60 JAKARTA PUSAT 10221")
print("          INDONESIA")

p = int(input("Nilai 1 : "))
w = int(input("Nilai 2 : "))

jum = p * w
print(jum)


data = [
    {"unit": 1, "harga": 500}
]

total = 0
for item in data:
    total += item["unit"] * item["harga"]

ppn = total * 0.10
print("Total :", total)
print("PPN   :", ppn)
print("Bayar :", total + ppn)


faktur = {
    "perusahaan": {
        "nama": "PT. SAMPLE INDONESIA",
        "alamat": "Jl. Jend Sudirman No.43, Jakarta Utara",
        "telp": "(021) 669 6666"
    },
    "faktur": {
        "no": "00000456",
        "tanggal": "11 Februari 2013",
        "due_date": "11 Februa_



