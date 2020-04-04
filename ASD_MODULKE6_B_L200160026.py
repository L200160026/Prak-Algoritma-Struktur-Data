#Author : Ridwan Renaldi (L200160026)
#Kelas  : B
#Python 3.6


def gabungkanDuaListUrut(A, B):
    la = len(A); lb = len(B)
    C = list()
    i = 0; j = 0

    while i < la and j < lb:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    while i < la:
        C.append(A[i])
        i += 1
    while j < lb:
        C.append(B[j])
        j += 1
    return C

#a = [2,8,15,23,37]
#b = [4,6,15,20]
#print (gabungkanDuaListUrut(a,b))

def mergeSort(A):
    if len(A) > 1:
        mid = len(A)//2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]
        mergeSort(separuhKiri)
        mergeSort(separuhKanan)

        i=0 ; j=0 ; k=0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j]:
                A[k] = separuhKiri[i]
                i = i + 1
            else:
                A[k] = separuhKanan[j]
                j = j + 1
            k=k+1

        while i < len(separuhKiri):
            A[k] = separuhKiri[i]
            i = i + 1
            k = k + 1
        while j < len(separuhKanan):
            A[k] = separuhKanan[j]
            j = j + 1
            k = k + 1

##c = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
##dd = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
##mergeSort(c)
##print (c)

def partisi(A, awal, akhir):
    nilaiPivot = A[awal]

    penandaKiri = awal + 1
    penandaKanan = akhir

    selesai = False
    while not selesai:
        while penandaKiri <= penandaKanan and A[penandaKiri] <= nilaiPivot:
            penandaKiri = penandaKiri + 1

        while A[penandaKanan] >= nilaiPivot and penandaKanan >= penandaKiri:
            penandaKanan = penandaKanan - 1

        if penandaKanan < penandaKiri:
            selesai = True
        else:
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanan]
            A[penandaKanan] = temp

    temp = A[awal]
    A[awal] = A[penandaKanan]
    A[penandaKanan] = temp

    return penandaKanan

def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah - 1)
        quickSortBantu(A, titikBelah + 1, akhir)

def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1)
    
#d = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
#quickSort(d)
#print (d)
    
#================================[TUGAS MAHASISWA]==============================
print ("================================[NO_1]==============================")
class MhsTIF():
    def __init__(self, nama, nim, kota, uang, Next=None):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uang = uang
        self.Next = None
    def __str__(self):
        return ("\nNama\t: "+ self.nama +\
                "\nNIM\t: "+ str(self.nim) +\
                "\nKota\t: "+ self.kota +\
                "\nUang\t: RP."+ str(self.uang))

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

    
def mergeSortModif(A):
    obj = A
    try:
        new = []
        for x in A:
            new.append(x.nim)
        A = new
    except:
        A = A
        
    if len(A) > 1:
        mid = len(A)//2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]
        mergeSortModif(separuhKiri)
        mergeSortModif(separuhKanan)

        i=0 ; j=0 ; k=0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j]:
                A[k] = separuhKiri[i]
                i = i + 1
            else:
                A[k] = separuhKanan[j]
                j = j + 1
            k=k+1

        while i < len(separuhKiri):
            A[k] = separuhKiri[i]
            i = i + 1
            k = k + 1
        while j < len(separuhKanan):
            A[k] = separuhKanan[j]
            j = j + 1
            k = k + 1
    try:
        hasil = []
        for x in range(len(A)):
            for i in range(len(A)):
                if A[x] == obj[i].nim:
                    hasil.append(obj[i])
        return hasil
    except:
        pass

print("[Merge Sort]")  
daftar1 = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
#print (mergeSortModif(daftar1))
for x in mergeSortModif(daftar1):
    print (x.nim)





    
def quickSortModif(A):
    obj = A
    try:
        new = []
        for x in A:
            new.append(x.nim)
        A = new
    except:
        A = A
        
    quickSortBantu(A, 0, len(A) - 1)
    
    try:
        hasil = []
        for x in range(len(A)):
            for i in range(len(A)):
                if A[x] == obj[i].nim:
                    hasil.append(obj[i])
        return hasil
    except:
        pass

print("\n[Quick Sort]")
daftar2 = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
#print(quickSortModif(daftar2))
for x in quickSortModif(daftar2):
    print (x.nim)


print ("\n================================[NO_2]==============================")
print ("Jawaban Ada di PDF")


print ("\n================================[NO_3]==============================")
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


from time import time as detak
from random import shuffle as kocok
import time

k = [x for x in range(1,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]
u_mrg = k[:]
u_qck = k[:]


aw = detak()
bubbleSort(u_bub)
ak = detak()
print ("Bubble : %g detik" %(ak-aw))

aw = detak()
selectionSort(u_sel)
ak = detak()
print ("Selection : %g detik" %(ak-aw))

aw = detak()
insertionSort(u_ins)
ak = detak()
print ("Insertion : %g detik" %(ak-aw))

aw = detak()
mergeSort(u_mrg)
ak = detak()
print("Merge : %g detik" %(ak-aw))

aw = detak()
quickSort(u_qck)
ak = detak()
print("Quick : %g detik" %(ak-aw))


print ("\n================================[NO_4]==============================")
print ("Jawaban Ada di PDF")


print ("\n================================[NO_5]==============================")
def mergeSort2(A):
    mergeSortBantu(A, 0, len(A)-1)

def mergeSortBantu(A, awal, akhir):
    mid = (awal+akhir)//2
    if awal < akhir:
        mergeSortBantu(A, awal, mid)
        mergeSortBantu(A, mid+1, akhir)

        i = 0 ; j = awal ; k = mid + 1
        tmp = [None] * (akhir - awal + 1)
        while j <= mid and k <= akhir:
            if A[j] < A[k]:
                tmp[i] = A[j]
                j = j + 1
            else:
                tmp[i] = A[k]
                k = k + 1
            i = i + 1

        if j <= mid:
            tmp[i:] = A[j:mid + 1]
        if k <= akhir:
            tmp[i:] = A[k:akhir + 1]
        i = 0
        while awal <= akhir:
            A[awal] = tmp[i]
            awal = awal + 1
            i = i + 1

n = [1,9,2,8,3,7,4,6,5]
mergeSort2(n)
print(n)


print ("\n================================[NO_6]==============================")
def quickSort2(arr):
    kurang = []
    pivotList = []
    lebih = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                kurang.append(i)
            elif i > pivot:
                lebih.append(i)
            else:
                pivotList.append(i)
        kurang = quickSort2(kurang)
        lebih = quickSort2(lebih)
        return kurang + pivotList + lebih

data = [1,9,2,8,3,7,4,6,5,10,15,11,14,12,13]
print (quickSort2(data))


print ("\n================================[NO_7]==============================")
u_mrg2 = k[:]
u_qck2 = k[:]


aw = detak()
mergeSort2(u_mrg2)
ak = detak()
print("Merge_2 : %g detik" %(ak-aw))

aw = detak()
quickSort2(u_qck2)
ak = detak()
print("Quick_2 : %g detik" %(ak-aw))


print ("\n================================[NO_8]==============================")
class Node():
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode


def cetak(head):
    curr = head
    while curr is not None:
        try:
            print (curr.data)
            curr = curr.nextNode
        except:
            pass

a = Node(1)
b = Node(3)
c = Node(5)
d = Node(7)
e = Node(6)
f = Node(4)
g = Node(2)

a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e
e.nextNode = f
f.nextNode = g

def mergeSortLinkedList(A):
    linked = A
    try:
        daftar = []
        curr = A
        while curr:
            daftar.append(curr.data)
            curr = curr.nextNode
        A = daftar
        #print (A)
    except:
        A = A

    if len(A) > 1:
        mid = len(A)//2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]
        mergeSortLinkedList(separuhKiri)
        mergeSortLinkedList(separuhKanan)

        i=0 ; j=0 ; k=0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j]:
                A[k] = separuhKiri[i]
                i = i + 1
            else:
                A[k] = separuhKanan[j]
                j = j + 1
            k=k+1

        while i < len(separuhKiri):
            A[k] = separuhKiri[i]
            i = i + 1
            k = k + 1
        while j < len(separuhKanan):
            A[k] = separuhKanan[j]
            j = j + 1
            k = k + 1

    for x in A:
        try:
            linked.data = x
            linked = linked.nextNode
        except:
            pass

mergeSortLinkedList(a)
cetak(a)

