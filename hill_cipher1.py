import numpy as np

P = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print('1. tao ma')
print('2. giai ma')
luachon = int(input('Nhap lua chon: '))

if luachon==1:
    kytu = str(input('Nhap ban tin ro: '))
    a = kytu.split()
    b = ''.join(a)
    # print(b)
    p = []
    for i in b:
        for j in range(0, 26):
            if i == P[j]:
                p.append(j)

    # print(p)

    m = int(input('Nhap so hang cua khoa: '))
    n = int(input('Nhap so cot cua khoa: '))
    khoa = str(input('Nhap khoa (nhap trong 1 hang): '))
    a1 = khoa.split()
    k = []
    for i in a1:
        # print(i)
        k.append(int(i))
    k = np.array(k)
    k = np.resize(k,(m,n))
    print(k)
    them = 0
    l = len(p)
    for i in range(0, 100):
        if l % m == 0:
            them = i
            break
        else:
            l = l + 1
    for i in range(0, them):
            p.append(25)
    # print(l)
    p = np.array(p)

    p = np.resize(p, (int(l/m),m))
    # print(p)
    # print(k)
    # print(k.shape)

    c = np.matmul(p, k)
    # print(c)

    kq = []
    for i in c:
        for j in i:
            kq.append(j)
    # print(kq)
    kq1 = []
    kq2 = []
    for i in kq:
        kq1.append(P[i%26].upper())
        kq2.append(i%26)
    print(kq2)
    ketqua = ''
    for i in kq1:
        ketqua = ketqua + str(i)
    # print(kq2)
    print('Ban tin mat: ',ketqua)
