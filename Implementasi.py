print "Belaar implementasi Membuat Keputusan di Python"
print "------------------------------------------------"
print "Kode Barang PRT001 = meja"
print "Kode Barang PRT002 = kursi"
print "Kode Barang PRT003 = Lemari"
a = raw_input ("Masukka Kode Barang : ")
b = 0
if (a == "PRT001"):
	b = 250000
	print "Harga = ",b
elif (a == "PRT002"):
	b = 100000
	print "Harga = ",b
elif (a == "PRT003"):
	b = 500000
	print "Harga = ",b
print "-----------------------"
c = input("Masukkan Jumlah Beli : ")
d = b * c
print "-----------------------"
print "total = ",d
