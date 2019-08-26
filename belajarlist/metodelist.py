hewan=["kelinci","panda","harimau","singa","ayam"]

# metode list yang di gunakan untuk menambah list

hewan.append("burung")
hewan.append("dinosaurus")

# append adalah metode yang di gunakan untuk menambahkan komponen di belakang

hewan.insert(0,"buaya")
hewan.insert(3,"kucing")

# insert adalah method yang di gunakan di untuk menyisipkan komponen list caranya masukan index baru komponen


hewan.extend("kadal")#maka akan menampilkan perhuruf artinya akan mengiterable k a d a l
hewan2=["kecoa","cacing"] #maka akan menampilkan iterable dari anggota list

hewan.extend(hewan2)
print(hewan)

menghitung=hewan.count("kucing") #menghitung komponen yang ada di dalam list
menghitung2=hewan.count("burung")
print(menghitung2)
print(menghitung)
# count adalah method yang di gunakan untuk menghitung elemen yang ada di dalam list


nomor=hewan.index("burung")
print(nomor)