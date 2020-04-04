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

def swap(A, p, q):
    tmp  = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i] < A[posisiTerkecil]:
            posisiTerkecil = i
    return posisiTerkecil

def bubbleSort(A):
    n = len(A)
    for i in range(n):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A, j, j+1)

def selectionSort(A):
    n = len(A)
    for i in range(n):
        tmp = cariPosisiYangTerkecil(A, i, n)
        if tmp != i:
            swap(A, tmp, i)

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai
        
L = [10,51,2,18,4,31,13,5,23,64,29]
insertionSort(L)
#print (L)

def cekNim(A):
    for i in A:
        print (i.nim)

#=====[NO_1]=====
print ("==========[NO-1]==========")
def urutkanNIM(obj):
    n = len(obj)
    for i in range(1, n):
        nilai = obj[i]
        pos = i
        while pos > 0 and nilai.nim < obj[pos-1].nim:
            obj[pos] = obj[pos-1]
            pos = pos-1
        obj[pos] = nilai

urutkanNIM(daftar)
cekNim(daftar)


#=====[NO_2]=====
print ("==========[NO-2]==========")
def urutAB(A, B):
    daftar = []
    loop = 0
    n1 = len(A)
    n2 = len(B)
    if n1 > n2:
        for x in A:
            try:
                if x < B[loop]:
                    daftar.append(x)
                    daftar.append(B[loop])
                    loop += 1
                else:
                    daftar.append(B[loop])
                    daftar.append(x)
                    loop += 1
            except:
                daftar.append(x)
    else:
        for x in B:
            try:
                if x < A[loop]:
                    daftar.append(x)
                    daftar.append(A[loop])
                    loop += 1
                else:
                    daftar.append(A[loop])
                    daftar.append(x)
                    loop += 1
            except:
                daftar.append(x)
    return daftar
        
    
d1 = [1,4,5,6,10,11,12]
d2 = [2,3,7,8,9]
print(urutAB(d1,d2))


#=====[NO_3]=====
print ("==========[NO-3]==========")
from time import time as detak
from random import shuffle as kocok

k = [x for x in range(1,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak()
bubbleSort(u_bub)
ak = detak()
print ("Bubble %g detik" %(ak-aw))

aw = detak()
selectionSort(u_sel)
ak = detak()
print ("Selection %g detik" %(ak-aw))

aw = detak()
insertionSort(u_ins)
ak = detak()
print ("Insertion %g detik" %(ak-aw))
