import numpy as np
P = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
C = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
while True:
    print('1. tao ma')
    print('2. giai ma')
    luachon = int(input('Nhap lua chon: '))

    if luachon==1:
        kytu = str(input('Nhap ban tin ro: '))
        a = kytu.split()
        b = ''.join(a)
        c = []
        for i in b:
            for j in range(0, 26):
                if i.lower() == P[j]:
                    c.append(int(j))
        l = len(c)
        k = str(input('Nhap khoa k: '))
        a1 = k.split()
        b1 = ''.join(a1)
        e =[]
        kq = []
        for i in b1:
            for j in range(0, 26):
                if i.lower() == P[j]:
                    e.append(int(j))
        for i in range(0,100):
            if l > len(e):
                e=np.concatenate((e, e))
            else:
                break
        mn = []
        for i in range(0, l):
            kq.append(C[(e[i]+c[i])%26])
            mn.append((e[i]+c[i])%26)
        m=''
        for i in range(0, l):
            m = m +str(kq[i])
        print('Ban tin mat: ',m)
        print(mn)

    if luachon==2:


        kytu = str(input('Nhap ban tin ro: '))
        a = kytu.split()
        b = ''.join(a)
        c = []
        for i in b:
            for j in range(0, 26):
                if i.lower() == P[j]:
                    c.append(int(j))
        l = len(c)
        k = str(input('Nhap khoa k: '))
        a1 = k.split()
        b1 = ''.join(a1)
        e = []
        kq = []
        for i in b1:
            for j in range(0, 26):
                if i.lower() == P[j]:
                    e.append(int(j))
        for i in range(0, 100):
            if l > len(e):
                e = np.concatenate((e, e))
            else:
                break
        mn = []
        for i in range(0, l):
            kq.append(P[(c[i] - e[i]) % 26])
            mn.append((c[i] - e[i]) % 26)
        m = ''
        for i in range(0, l):
            m = m + str(kq[i])
        print('Ban tin mat: ', m)
        print(mn)





