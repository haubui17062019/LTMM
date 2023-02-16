import numpy as np
def nghich_dao_mod(n,r):
    for i in range(0,10000):
        x = (int(n)*i + 1)%int(r)
        if(x == 0):
            return((int(n)*i+1)/int(r))
            break

def tinh_mod(r,b1,n):
    rb = r*b1 // n
    t = r*b1 - rb*n
    return t

def knapsacksum(l1, x1, a = []):
    k = 0
    x2 = list(x1)
    for i in range(0,l1):
        k = k + int(a[i])*int(x2[i])
    return k
def inv_knapsacksum(l1, s1,a = []):
    inv = []
    i = l1 - 1
    while(i >= 0):
        if s1 >= a[i]:
            s1 = s1-a[i]
            inv.append(1)
        else:
            inv.append(0)
        i = i-1
    inv = inv[::-1]
    return inv
'''''''''
r = 41
n = 1001
b = [7,11,23,43,87,173,357]
h = [7,6,5,1,2,3,4]
'''''''''
print("MA HOA KNAPSNAK")

r = input("nhap r: ")
n = input("nhap n: ")
try:
    n1 = int(input("Nhap so phan tu cua b: "))
    if n1 <= 0:
        exit()
except:
    print('Phai nhap so tu nhien')
    exit()

b = []

for i in range(n1):
    b.append(int(input('Nhap so thu %d: ' % (i+1))))
print(b)
print('nhap hoan vi: ')
h = []
for i in range(0, len(b)):
    h.append(input('Nhap so thu %d: ' % (i+1)))

#ma hoa plaintext
t2 = []
t2 = input("nhap plaintext: ")
text = []
for i in range(0,len(t2)):
    text.append(ord(t2[i]))
text1 = []
for i in range(0,len(t2)):
    t1 = format(text[i], "b")
    for i in range(len(t1),7):
        t1 = '0' + t1
    text1.append(t1)

print('ma hoa text: ',text1)

t3 = []
for i in range(0, len(b)):
    t3.append(tinh_mod(int(r), int(b[i]), int(n)))
print('t: ',t3)


#tinh a
a = []
print('h: ',h)
for i in range(0, len(b)):
    a.append(t3[int(h[i])-1])
#print('a: ',a)

#tinh ham knapsacksum:
l1 = len(b)
s = []
for i in range(0,len(text1)):
    s.append(knapsacksum(l1, text1[i], a))
print('ma hoa cua:', t2,': ',s)

#tim s'
s1 = []
for i in range(0, len(text1)):
    #print(nghich_dao_mod(n,r))
    s1.append(tinh_mod(int(nghich_dao_mod(n,r))*int(s[i]),1, int(n)))

#print('s1: ',s1)

#tim x'
x1 = []
for i in range(0, len(text1)):
    x1.append(inv_knapsacksum(l1, int(s1[i]), b))

#print('ma hoa:? ',x1)
#tim x

x4 = []
for i in range(0, len(text1)):
    for j in range(0, len(b)):
        x4.append(x1[i][int(h[j])-1])
k1 = []
x2 = np.array(x4)
x3 = np.array_split(x2, len(text1))
#print(x3)
for i in range(0,len(text1)):
    k = 0
    for j in range(0, len(b)):
        k = k + (2**(len(b)-1-j))*x3[i][j]
    k1.append(k)
#print(k1)
gm = []
for i in range(0,len(text1)):
    gm.append(chr(k1[i]))

gm1 = "".join(gm)

print('giai ma:',gm1)




