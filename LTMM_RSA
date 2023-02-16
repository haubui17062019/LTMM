def nghich_dao_mod(n,r):
    #return = r^-1 mod(n)
    for i in range(0,10000):
        x = (int(n)*i + 1)%int(r)
        if(x == 0):
            return int(((int(n)*i+1)/int(r)))
            break

def tinh_mod(b1,n):
    # return = b1 mod(n)
    rb = b1 // n
    t = b1 - rb*n
    return t
#chon 2 so p,q:
print("nhap hai so nguyen to lon khac nhau: ")
while True:
    p = int(input('nhap p:'))
    count = 0
    for i in range(1, p + 1):
        if p % i == 0:
            count += 1
    if count != 2:
        print('nhap lai')
    else:
        break

while True:
    q = int(input('nhap q:'))
    count = 0
    for i in range(1, q + 1):
        if q % i == 0:
            count += 1
    if count != 2 or q == p:
        print('nhap lai')
    else:
        break
n = p*q
phi = (p-1)*(q-1)
print('phi:',phi)

#chon e:
while True:
    e = int(input('nhap e nguyen to voi phi:'))
    e1 = e
    phi1 = phi
    while(e1 != phi1):
        if(e1 > phi1):
            e1 = e1 - phi1
        else:
            phi1 = phi1 -e1
    if( e1 != 1):
        print('nhap lai')
    else:
        break

#tim d:
d = nghich_dao_mod(phi,e)

#cac khoa:
print('khoa cong khai(e,n):',e,',',n)
print('khoa bi mat(d,n)',d,',',n)

#nhap ban tin ro:
t2 = []
t2 = input("nhap plaintext: ")
text = []
for i in range(0,len(t2)):
    text.append(ord(t2[i]))
print(text)
#ma hoa: C = M^e (mod n)
ma = []
for i in range(0,len(text)):
    ma.append(tinh_mod(text[i]**e,n))

print('ma hoa:', ma)

#giai ma: M = C^d (mod n)
tin = []
for i in range(0,len(text)):
    tin.append(chr(tinh_mod(ma[i]**d, n)))

gm1 = "".join(tin)
print('giai ma:',gm1)



