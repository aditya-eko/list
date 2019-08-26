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
nomor2=hewan.index("kecoa")

print(nomor)
print(nomor2)

# index di gunakan untuk mengetahui index ke berapa dari sebuah komponen

hewan.reverse()
print(hewan)

# reverse di gunakan untuk membalikan sebuah urutan

hewan.sort()
print(hewan)

# sort di gunakan untuk mengurutkan berdasarkan abjad

hasil=hewan.copy()
print(hasil)
print(hasil)
# copy di gunakan untuk mengcopy list




hewan.pop()
hewan.pop(0)
hewan.pop(0)

print(hewan)

# pop menghapus komponen yang ada di belakang atau bisa dengan memasukan indexnya

hewan.remove("buaya")
hewan.remove("ayam")
print(hewan)
# remove menghapus komponen berdasarkan item

hewan.clear()
print(hewan)

# clear menghapus semua tipe data list