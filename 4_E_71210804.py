#input
a = int (input("masukan suku pertama : "))
r = int (input("masukan rasio : "))
n = int (input("masukan suku yang dicari : "))

#proses
Sn = (a * r ** n-1)/(r-1) 

#cetak di layar
print ("jumlah suku ke 11 dari deret 1,3,9,27,81", Sn)