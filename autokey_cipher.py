P = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
C = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
key = []
key1 = 0
while True:
    print('1. Tao ma')
    print('2. Giai ma')
    luachon = int(input('Nhap lua chon: '))

    if luachon==1:
        kytu=str(input('nhap ban tin ro: '))
        k = int(input('Nhap khoa k: '))
        key1 = k
        a = kytu.split()
        b = ''.join(a)
        c = []
        e =[]
        for i in b:
            for j in range(0, 26):
                if i.lower() == P[j]:
                    c.append(int(j))
        d = c.copy()
        d.insert(0, k)
        del d[len(d)-1]
        key = d.copy()
        for i in range(0,len(c)):
            e.append((c[i]+d[i])%26)
        kq = []
        for i in range(0, len(e)):
             kq.append(C[e[i]])
        m = ''
        for i in range(0, len(kq)):
            m = m + str(kq[i])
        print('Ban tin mat: ',m)
    if luachon==2:
        kytu = str(input('nhap ban tin mat: '))
        k = int(input('Nhap khoa k: '))
        if k != key1:
            print('nhap sai k')
            break
        a = kytu.split()
        b = ''.join(a)
        c = []
        e = []
        for i in b:
            for j in range(0, 26):
                if i.upper() == C[j]:
                    c.append(int(j))


        for i in range(0, len(c)):
            e.append((c[i] - key[i]) % 26)
        kq = []
        for i in range(0, len(e)):
            kq.append(C[e[i]])
        m = ''
        for i in range(0, len(kq)):
            m = m + str(kq[i])
        print('Ban tin ro: ', m)
        # kytu=str(input('nhap ban tin mat: '))
        # k = str(input('Nhap khoa k: '))
        # d = k.split()
        # f = []
        # for i in d:
        #     f.append(int(i))
        # a = kytu.split()
        # b = ''.join(a)
        # c = []
        # e =[]
        # for i in b:
        #     for j in range(0, 26):
        #         if i.upper() == C[j]:
        #             c.append(int(j))
        # if len(c) == len(f):
        #     for i in range(0,len(c)):
        #         e.append((c[i]-f[i])%26)
        #     kq = []
        #     for i in range(0, len(e)):
        #          kq.append(P[e[i]])
        #     m = ''
        #     for i in range(0, len(kq)):
        #         m = m + str(kq[i])
        #     print('Ban tin ro: ',m)
        # else:
        #     print('Nhap sai')
        #
        #
        #
        #
        #
        #
