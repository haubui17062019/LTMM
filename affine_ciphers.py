P = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
C = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
K = [1,3,5,7,9,11,15,17,19,21,23,25]
while True:
    a=[]
    b=[]
    c=[]
    kq=[]
    print('1. tao ma')
    print('2. giai ma')
    luachon = int(input('Nhap lua chon: '))
    if luachon == 1:
        kytu = str(input('Nhap ban tin ro: '))
        k1 = int(input('Nhap khoa k1: '))
        k2 = int(input('Nhap khoa k2: '))
        if k1 not in K:
            print('Nhap sai khoa k1')
            exit()
        a=kytu.split()
        b=''.join(a)
        for i in b:
            c.append(i.lower())
        e = []
        for i in range(0, len(c)):
            for j in range(0, 26):
                if P[j] == c[i]:
                    kq.append(P[(j*k1+k2)%26].upper())
                    e.append((j*k1+k2)%26)
        print('Ban tin mat: ',''.join(kq))

    if luachon == 2:
        kytu = str(input('Nhap ban tin mat: '))
        k1 = int(input('Nhap khoa k1: '))
        k2 = int(input('Nhap khoa k2: '))
        if k1 not in K:
            print('Nhap sai khoa k1')
            exit()
        for i in range(1, 100):
            d = (k1*i)%26
            if d == 1:
                k1 = i
                break
        a = kytu.split()
        b = ''.join(a)
        for i in b:
            c.append(i.upper())
        for i in range(0, len(c)):
            for j in range(0,26):
                if c[i] == C[j]:
                    kq.append(C[((j-k2)*k1)%26].lower())
        print('Ban tin ro: ',''.join(kq))











