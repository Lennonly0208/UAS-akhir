print ("Tugas UAS Akhir") 
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