#Author : Ridwan Renaldi (L200160026)
#Kelas  : B
#Python 3.6

import re


print ("\nNO_1")
f = open('Indonesia.txt', 'r' , encoding='UTF8')
p= r'\sMe\w+|\sme\w+'
data = re.findall(p, f.read())
print (data)
f.close()


print ("\nNO_2")
f = open('Indonesia.txt', 'r' , encoding='UTF8')
p= r'\sDi\w+|\sdi\w+'
data = re.findall(p, f.read())
print (data)
f.close()


print ("\nNO_3")
f = open('Indonesia.txt', 'r' , encoding='UTF8')
p= r'Di\s\w+|di\s\w+'
data = re.findall(p, f.read())
print (data)
f.close()


print ("\nNO_4_A")
f = open('KEI.html', 'r' , encoding='UTF8')
txt = f.read()
data = re.findall(r'">(\w.+)</a></td>\n', txt)
print (data)
f.close()


print ("\nNO_4_B")
f = open('KEI.html', 'r' , encoding='UTF8')
txt = f.read()
data1 = re.findall(r'<td>[0-9.]+</td>\n<td>[0-9.]+</td>\n<td>[0-9.]+</td>\n<td>([0-9.]+)</td>', txt)
data2 = re.findall(r'<td>n/a</td>\n<td>n/a</td>\n<td>[0-9.]+</td>\n<td>([0-9.]+)</td>', txt)
hasil = data1+data2
print (hasil)
f.close()


print ("\nNO_4_C")
f = open('KEI.html', 'r' , encoding='UTF8')
txt = f.read()
data1 = re.findall(r'">(\w.+)</a></td>\n<td>[0-9.]+</td>\n<td>[0-9.]+</td>\n<td>[0-9.]+</td>\n<td>([0-9.]+)</td>', txt)
data2 = re.findall(r'">(\w.+)</a></td>\n<td>n/a</td>\n<td>n/a</td>\n<td>[0-9.]+</td>\n<td>([0-9.]+)</td>', txt)
total = data1+data2

hasil = []
for i in total:
    hasil.append((i[0], float(i[1])))

print(hasil)
f.close()
