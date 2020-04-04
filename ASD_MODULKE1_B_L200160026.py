#AUTHOR : RIDWAN RENALDI (L200160026)
#Kelas  : B
#Python 3.6

def cetakSiku(x):
    try:
        x = int(x)+1
        cetak = ""
        for i in range(x):
            cetak += (i * "*") + "\n"
        return print(cetak)
    except Exception as e:
        print (e)


def persegiEmpat(xy):
    try:
        splt = xy.split(",")
        x = int(splt[0])
        y = int(splt[1])
        cetak = "@"*y+"\n"
        for i in range(x-2):
            cetak += "@" + (y-2)*" " + "@\n"
        cetak += "@"*y
        return print(cetak)
    except Exception as e:
        print (e)


def jumlahHurufVokal(kata):
    try:
        kata = kata.lower()
        jmlh = len(kata)
        jmlhVokal = 0
        konsonan = 0
        vokal = ["a","i","u","e","o"]
        simbol = """ `~!@#$%^&*()_-+=|\}]{["':;<,>.?/1234567890"""
        for i in kata:
            if i in vokal:
                jmlhVokal += 1
            else:
                if i in simbol:
                    pass
                else:
                    konsonan += 1
        return print ("Jumlah karakter: "+str(jmlh)+"\nJumlah huruf vokal: "+str(jmlhVokal)+"\nJumlah Konsonan: "+str(konsonan)+"\nJumlah huruf: "+str(jmlhVokal+konsonan))
    except Exception as e:
        print (e)


def rerata(Input):
    nilai = Input.split(",")
    total = 0
    for i in nilai:
        total += int(i)
    hasil = total/len(nilai)
    return print("Rata-rata : ",hasil)


def apakahPrima(n):
    try:
        n = int(n)
        if n > 1:
            for i in range(2,n):
                """
                [+] Melakukan pengecekan dengan perulangan hasil sisa bagi
                [+] Apabila kondisi if terpenuhi maka angka tersebut dapat dibagi
                    dengan faktor sehingga bukan merupakan bilangan prima
                [+] Apabila kondisi if tidak terpenuhi sampai perulangan habis
                    maka akan masuk pada kondisi else (yg berada di bawah for)
                """
                if (n % i) == 0:
                    pass
                    break
            else:
                return n
        else:
            pass
    except Exception as e:
        print (e)


def cekPrima(xy):
    try:
        splt = xy.split("-")
        x = int(splt[0])
        y = int(splt[1])
        prima = []
        for i in range(x,y+1):
            if apakahPrima(i) == None:
                pass
            else:
                prima.append(apakahPrima(i))
        return print ("Bilangan Prima antara "+xy+" : ",prima)
    except Exception as e:
        print (e)

def faktorPrima(n):
    try:
        n = int(n)
        faktor = []
        if n > 1:
            for i in range(2,n):
                if (n % i) == 0:
                    faktor.append(i)
            else:
                faktor.append(n)
        print ("Faktor dari angka "+str(n)+" : ",faktor)
    except Exception as e:
        print (e)


def apakahTerkandung(x,y):
    word = x
    sentence = y
    x = x.lower()
    y = y.lower()
    if x in y:
        kata = "Kata ["+word+"] terkandung dalam kalimat ini ["+sentence+"]"
    else:
        kata = "Kata ["+word+"] tidak terkandung dalam kalimat ini ["+sentence+"]"
    return print(kata)


def cetakAngka(xy):
    splt = xy.split("-")
    x = int(splt[0])
    y = int(splt[1])
    for i in range(x,y+1):
        if i%3 == 0 and i%5 == 0:
            print ("Python UMS")
        elif i%3 == 0:
            print ("Python")
        elif i%5 == 0:
            print ("UMS")
        else:
            print (i)

from math import sqrt as akar
def selesaikanABC(abc):
    abc = abc.split(",")
    a = float(abc[0])
    b = float(abc[1])
    c = float(abc[2])
    D = b**2 - 4*a*c
    if D < 0:
        return print ("Determinannya negatif. Persamaan tidak mempunyai akar real.")
    else:
        x1 = (-b + akar(D))/(2*a)
        x2 = (-b - akar(D))/(2*a)
        hasil = (x1, x2)
        return print("Hasil = " + str(hasil))


def apakahKabisat(thn):
    thn = int(thn)
    if thn%400 == 0 or thn%4 == 0:
        if thn%100 == 0:
            print (thn," bukan tahun kabisat")
        else:
            print (thn," adalah tahun kabisat")
    else:
        print (thn," bukan tahun kabisat")


import random
def tebakAngka():
    angka = random.choice(range(1,101))
    print (".:[PERMAINAN TEBAK ANGKA]:.\n* Tebak Angka antara 1-100\n* Kesempatan hanya 5x")
    loop = 1
    while True:
        n = int(input("Masukkan tebakan ke-"+str(loop)+": "))
        if n == angka:
            print ("Tebakan anda benar!")
            break
        elif n > angka:
            print ("Angka itu terlalu besar. Coba lagi")
        elif n < angka:
            print ("Angka itu terlalu kecil. Coba lagi")
        else:
            print ("Masukkan Angka!!")
        if loop == 5:
            print ("Anda Kalah!\nJawaban yang benar adalah ",angka)
            break
        loop += 1


def Katakan(angka):
    jmlh = len(angka)
    satuan = ["satu", "dua", "tiga", "empat", "lima",
              "enam", "tujuh", "delapan", "sembilan", "sepuluh",
              "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas",
              "enam belas", "tujuh belas", "delapan belas", "sembilan belas"
              ]
    angka = '{:0,.0f}'.format(int(angka))
    angka = angka.split(",")
    katakan = []
    idx = 1
    if jmlh < 10:
        for x in angka[::-1]:
            seribu = False
            if idx == 2 and x[-1]!="0":
                if int(x)< 2 :
                    katakan.append("seribu")
                    seribu = True
                else:
                    katakan.append("ribu")
            if idx == 3 and x[-1]!="0":
                katakan.append("juta")
            if seribu == False:
                if int(x[-2:])<20 and int(x[-2:])>0:
                    katakan.append(satuan[int(x[-2:])-1])
                elif int(x[-2:])>0:
                    if int(x[-1])!=0:
                        katakan.append(satuan[int(x[-1])-1])
                    if int(x[-2]) != 0:
                        katakan.append(satuan[int(x[-2])-1]+" puluh")
            if int(x[0]) > 2 and len(x)==3 :
                katakan.append(satuan[int(x[0])-1]+" ratus")
            elif len(x)==3 and int(x[0])!=0 :
                katakan.append("seratus")
            idx+=1
        return print(" ".join(katakan[::-1]))
    else:
        return print("Angka harus dibawah satu milyar!")

def formatRupiah(num):
    num = int(num)
    rupiah = "{:,}".format(num)
    hasil = rupiah.replace(",",".")
    print ("Rp",hasil)
        

pilihan ="""\n===========================
SILAHKAN PILIH SESUAI NOMOR
===========================
1. Cetak Siku
2. Persegi Empat
3. Huruf Vokal
4. Rata-rata
5. Cek Prima
6. Mencari Bil Prima
7. Faktor Prima
8. Apakah Terkandung
9. Cetak Angka Kelipatan
10. Determinan
11. Kabisat
12. Tebak Angka
13. Katakan
14. Format Rupiah

0. Exit
===========================
"""

try:
    while True:
        print (pilihan)
        
        try:
            angka = int(input("Masukkan angka pilihan anda : "))
        except:
            angka = 0
            print ("Masukkan Angka Bukan Huruf!")
        if angka == 1:
            print ("[Example] = 45")
            Input = input("Masukkan angka : ")
            cetakSiku(Input)
        elif angka == 2:
            print ("[Example] = 4,5")
            Input = input("Masukkan angka : ")
            persegiEmpat(Input)
        elif angka == 3:
            print ("[Example] = Hello World")
            Input = input("Masukkan sebuah kalimat : ")
            jumlahHurufVokal(Input)
        elif angka == 4:
            print ("[Example] = 4,6,12,5,23,1,9")
            Input = input("Masukkan angka : ")
            rerata(Input)
        elif angka == 5:
            print ("[Example] = 23")
            Input = input("Masukkan angka : ")
            if apakahPrima(Input)== None:
                print ("Angka "+Input+" = Bukan Bilangan Prima")
            else:
                print ("Angka "+Input+" = Bilangan Prima")
        elif angka == 6:
            print ("[Example] = 1-100")
            Input = input("Masukkan angka : ")
            cekPrima(Input)
        elif angka == 7:
            print ("[Example] = 120")
            Input = input("Masukkan angka : ")
            faktorPrima(Input)
        elif angka == 8:
            print ("[Example] :\nKata : solo\nKalimat : Saya tinggal di solo")
            Input1 = input("Masukkan kata : ")
            Input2 = input("Masukkan kalimat : ")
            apakahTerkandung(Input1,Input2)
        elif angka == 9:
            print ("[Example] = 1-100")
            Input = input("Masukkan angka : ")
            cetakAngka(Input)
        elif angka == 10:
            print ("[Example] = 2,6,3")
            Input = input("Masukkan angka : ")
            selesaikanABC(Input)
        elif angka == 11:
            print ("[Example] = 1896")
            Input = input("Masukkan tahun : ")
            apakahKabisat(Input)
        elif angka == 12:
            tebakAngka()
        elif angka == 13:
            print ("[Example] = 32540231")
            Input = input("Masukkan angka : ")
            Katakan(Input)
        elif angka == 14:
            print ("[Example] = 2560000")
            Input = input("Masukkan angka : ")
            formatRupiah(Input)
        elif angka == 0:
            break
        else:
            print ("Angka tidak ada dalam daftar!")

except Exception as e:
    print (e)


