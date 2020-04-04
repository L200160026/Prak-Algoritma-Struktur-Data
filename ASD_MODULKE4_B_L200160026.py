#Author : Ridwan Renaldi (L200160026)
#Kelas : B
#Python 3.6

class MhsTIF():
    def __init__(self, nama, nim, kota, uang, Next=None):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uang = uang
        self.Next = None
    def __str__(self):
        return (self.nama)

c0 = MhsTIF('Ika',10,'Sukoharjo',240000)
c1 = MhsTIF('Budi',51,'Sragen',230000)
c2 = MhsTIF('Ahmad',2,'Surakarta',250000)
c3 = MhsTIF('Chandra',18,'Surakarta',235000)
c4 = MhsTIF('Eka',4,'Boyolali',240000)
c5 = MhsTIF('Fandi',31,'Salatiga',250000)
c6 = MhsTIF('Deni',13,'Klaten',245000)
c7 = MhsTIF('Galuh',5,'Wonogiri',245000)
c8 = MhsTIF('Janto',23,'Klaten',245000)
c9 = MhsTIF('Hasan',64,'Karanganyar',270000)
c10 = MhsTIF('Khalid',29,'Purwodadi',265000)

c0.Next = c1
c1.Next = c2
c2.Next = c3
c3.Next = c4
c4.Next = c5
c5.Next = c6
c6.Next = c7
c7.Next = c8
c8.Next = c9
c9.Next = c10
daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

#No1
def cari (listnya,inputan):
    index = []
    for x in range(len(listnya)):
        if listnya[x].nama == inputan:
            index.append(x)
        if listnya[x].nim == inputan:
            index.append(x)
        if listnya[x].kota == inputan:
            index.append(x)
        if listnya[x].uang == inputan:
            index.append(x)
    print (index)
#cari(daftar,"Klaten")

#No2
def cariTerkecil(listnya):
    uangterkecil = listnya[0].uang
    for x in listnya:
        if x.uang < uangterkecil:
            uangterkecil = x.uang
        else:
            pass
    print (uangterkecil)
#cariTerkecil(daftar)

#No3
def cariTerkecilOBJ(listnya):
    uangterkecil = listnya[0].uang
    obj = []
    for x in listnya:
        if x.uang < uangterkecil:
            uangterkecil = x.uang
        else:
            pass
    index = []
    for i in range(len(listnya)):
        if listnya[i].uang == uangterkecil:
            index.append(i)
            
    print("Uang Terkecil : "+str(uangterkecil))
    print("Index : "+str(index))
#cariTerkecilOBJ(daftar)

#No4
def kurangDari(listnya):
    obj = []
    for x in listnya:
        if x.uang < 250000:
            obj.append(x.nama)
        else:
            pass
    return obj
#print(kurangDari(daftar))

#No5
def cariItem(objek,item):
    index = []
    objek = objek
    while objek is not None:
        if objek.nama == item:
            index.append(objek.nama)
        if objek.nim == item:
            index.append(objek.nama)
        if objek.kota == item:
            index.append(objek.nama)
        if objek.uang == item:
            index.append(objek.nama)
        objek = objek.Next
    print (index)
#cariItem(c0,"Klaten")



#No6
data = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,30]
def binSe1(kumpulan, target):
    low = 0
    high = len(kumpulan) - 1
    index = []
    while low <= high:
        mid = (high + low)//2
        if kumpulan[mid] == target:
            return mid
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
#print(binSe1(data, 13))

#No7
dataGanda = [3,5,7,11,11,11,11,11,11,11,15,15,15,21,21,21,21,27,27,29,34,35,35,35,40,45]
def binSe2(kumpulan, target):
    low = 0
    high = len(kumpulan) - 1
    index = []
    while low <= high:
        mid = (high + low)//2
        if kumpulan[mid] == target:
            mid1 = mid
            mid2 = mid-1
            while True:
                if kumpulan[mid2] == target:
                    index.append(mid2)
                    mid2 -= 1
                if kumpulan[mid1] == target:
                    index.append(mid1)
                    mid1 += 1
                else:
                    index.sort()
                    return index
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
        
    return False
#print(binSe2(dataGanda, 11))

#No8
import random
def tebakAngka():
    print ("==========[Game Tebak Angka]==========")
    awal = int(input("Masukkan angka awal : "))
    akhir = int(input("Masukkan angka akhir : "))
    data = [x for x in range(awal,akhir+1)]
    angka = random.choice(data)
    jmlh = len(data)
    kesempatan = 0
    while True:
        if jmlh == 1:
            kesempatan += 1
            break
        else:
            kesempatan += 1
            jmlh = jmlh//2
    print ("=======[Kesempatan menebak : %sx]=======" %(kesempatan))
    while True:
        n = int(input("Masukkan tebakan ke-"+str(kesempatan)+": "))
        if n == angka:
            print ("Tebakan anda benar!")
            break
        elif n > angka:
            print ("Angka itu terlalu besar. Coba lagi")
        elif n < angka:
            print ("Angka itu terlalu kecil. Coba lagi")
        else:
            print ("Masukkan Angka!!")
        if kesempatan == 1:
            print ("Anda Kalah!\nJawaban yang benar adalah ",angka)
            break
        kesempatan -= 1

#tebakAngka()
            
        



    
