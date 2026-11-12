#Operator

#Operator Aritmatika
a = 12
b = 5
c = 2

# 1. Penjumlahan
penjumlahan = a + b + c
sisabagi_penjumlahan = penjumlahan % b
print(f"hasil penjumlahan {a} + {b} + {c} = {penjumlahan}")
print(f"sisa bagi penjumlahan {penjumlahan} mod {b} = {sisabagi_penjumlahan}")

# 2. Perkalian
perkalian = a * b * c
sisabagi_perkalian = perkalian % b
print(f"hasil perkalian {a} * {b} * {c} = {perkalian}")
print(f"sisa bagi perkalian {perkalian} mod {b} = {sisabagi_perkalian}")

# 3. Pembagian
pembagian = a / b
sisabagi_pembagian = a % b
print(f"hasil pembagian {a} / {b} = {pembagian}")
print(f"sisa bagi pembagian {a} mod {b} = {sisabagi_pembagian}")

#Operator Assigment
a = 12
print(f"a awal = {a}")
a += 2 # a = a + 2
print(f"setelah a += 2, a = {a}")

#Operator Perbandingan
a = 14
b = 5
print(f"a = {a}, b = {b}")

perbandingan1 = a == b
print(f"a == b : {perbandingan1} -> apakah a sama dengan b?")
perbandingan2 = a != b
print(f"a != b : {perbandingan2} -> apakah a tidak sama dengan b?")
perbandingan3 = a > b
print(f"a > b : {perbandingan3} -> apakah a lebih besar dari b?")
perbandingan4 = a < b
print(f"a < b : {perbandingan4} -> apakah a lebih kecil dari b?")
perbandingan5 = a >= b
print(f"a >= b : {perbandingan5} -> apakah a lebih besar sama dengan b?")
perbandingan6 = a <= b
print(f"a <= b : {perbandingan6} -> apakah a lebih kecil sama dengan b?")

#Operator Logika AND
# pakai perbandingan5 (a >= b) yang hasilnya True, dan x yang udah kita buat
x = 3
perbandingan = perbandingan5
OpAnd = perbandingan and (x >= 2)
print(f"OpAnd = {OpAnd} -> True and True = True")

#Operator Logika OR
OpOr = perbandingan or (x >= 10)
print(f"OpOr = {OpOr} -> True or False = True")

#Operator Logika NOT
OpNot = not perbandingan
print(f"OpNot = {OpNot} -> not True = False")