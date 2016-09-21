import os

def garis():
	print "-" * 80

def ubah(x):
	if list_isi[x] == "1":
		list_isi[x] = "4"
	elif list_isi[x] == "2":
		list_isi[x] = "3"
	elif list_isi[x] == "3":
		list_isi[x] = "2"
	elif list_isi[x] == "4":
		list_isi[x] = "1"

file_skala1 = open("hasil skala 2.txt", "w")

fav = [1, 2, 3, 4, 17, 18, 19, 20, 9, 10, 11, 12]
x = 0
while x < len(fav):
	fav[x] = fav[x] - 1
	x += 1

garis()
petunjuk = """Isi SS dengan 1
Isi S dengan 2
Isi TS dengan 3
Isi STS dengan 4"""
print petunjuk
garis()

isi = raw_input("Masukkan jawaban aitem: ")
list_isi = list(isi)

y = 0
while y < len(fav):
	ubah(fav[y])
	y += 1

for x in list_isi:
	file_skala1.write(x+"\n")

garis()
print "Silahkan buka file 'hasil skala 2.txt'"
garis()

os.system("subl 'hasil skala 2.txt'")

# windows
# os.startfile("hasil skala 2.txt")

file_skala1.close()