#TODO:
#Anda diharuskan membuat program diskon untuk sebuah toko belanja dengan ketentuan berikut.
#- Jika pelanggan berbelanja lebih dari 500.000 ribu, mereka akan mendapat potongan harga 10%.
#- Seorang pelanggan bernama Dico telah berbelanja senilai 750.000 ribu.
#- Buat operasi aritmetika untuk menghitung total harga belanja Dico setelah mendapatkan diskon, 
# dan simpan dalam variabel bernama "total_harga".

#Jangan ubah kode ini 
dico = 70000

#cek jumlah belanja dico ada lebih dari 500.000 atau tidak
if dico > 500000:
    #menghitung diskon 10%
    diskon = 0.10 * dico
    
    #menghitung total harga setelah diskon
    total_harga = dico - diskon
else:
    #jika tidak ada dikon, maka harga akan sama dengan harga barang
    #yang dibeli dico
    total_harga = dico
    
#menampilkan hasil
print(total_harga)
    