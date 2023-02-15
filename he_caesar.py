P = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
C = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
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
        k = int(input('Nhap khoa k: '))
        a=kytu.split()
        b=''.join(a)
        for i in b:
            c.append(i.lower())
        for i in range(0, len(c)):
            for j in range(0, 26):
                if P[j] == c[i]:
                    if j+k<26:
                        kq.append(P[(j+k)%26].upper())
                    else:
                        kq.append(P[(j+k-26)%26].upper())
        print('Ban tin mat: ',''.join(kq))
    if luachon == 2:
        kytu = str(input('Nhap ban tin mat: '))
        k = int(input('Nhap khoa k: '))
        a = kytu.split()
        b = ''.join(a)
        for i in b:
            c.append(i.upper())
        for i in range(0, len(c)):
            for j in range(0,26):
                if c[i] == C[j]:
                    if j - k >=0:
                        kq.append(C[(j - k) % 26].lower())
                    else:
                        kq.append(C[(j - k + 26) % 26].lower())
        print('Ban tin ro: ',''.join(kq))











