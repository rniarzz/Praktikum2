print("Nama saya Rini Ariza")
print("Saya Belajar Python")

a = 240
b = 77
print("variable a = " , a)
print("variable a = " , b)
print("hasil perjumlahan a + b = " , a + b)

# input nilai variable
a = input ("masukkan nilai a: ")
b = input ("masukkan nilai b: ")

# cetak nilai variable
print("variable a:",a )
print("variable b:",b )

#cetak hasil operasi kedua variable dengan string format
print("hasil penggabungan {1}+{0}=%s".format(a,b) % (a+b))

# konversi nilai variable
a=int(a)
b=int(b)
print("Hasil penjumlahan {1}+{0}=%d".format(a,b) %(a+b))
print("Hasil pembagian {1}/{0}=%d".format(a,b) %(a/b))









