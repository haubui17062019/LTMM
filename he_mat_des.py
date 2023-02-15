pc1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

pc2 = [14, 17, 11, 24, 1, 5, 3, 28,
       15, 6, 21, 10, 23, 19, 12, 4,
       26, 8, 16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55, 30, 40,
       51, 45, 33, 48, 44, 49, 39, 56,
       34, 53, 46, 42, 50, 36, 29, 32]

hexa = ['0000', '0001', '0010', '0011', '0100',
        '0101', '0110', '0111', '1000', '1001',
        '1010', '1011', '1100', '1101', '1110',
        '1111']
text_hexa = ['0', '1', '2', '3', '4', '5', '6', '7',
              '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
#matran dich 1 bit
shift_pos = [1, 2, 9, 16]

sub_keys = []

round_text = []

#chon hang cua S-Box
s_rows = ['00', '01', '10', '11']

# chon cot cua S-Box
s_cols = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000',
          '1001', '1010', '1011', '1100', '1101', '1110', '1111']

ip = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

ip_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

ep = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,
      8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
      16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
      24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

p = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

s0 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
      [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
      [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

s1 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
      [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
      [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

s2 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
      [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]

s3 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
      [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
      [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

s4 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
      [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
      [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

s5 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
      [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
      [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
      [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

s6 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
      [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
      [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

s7 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
      [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
      [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
      [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

# chuyen ve 64 bit
def hextobin(x):
       return bin(int(x, 16))[2:].zfill(64)

# doi chieu qua pc1
def pc1conversion(keybin):
       keylist = []
       for i in keybin:
              keylist.append(int(i))
       newlist = []
       for i in pc1:
              newlist.append(keylist[i - 1])
       return newlist

# dich trai 1 bit
def leftshift_by1(x):
       return x[1:] + x[0:1]

# dich trai 2 bit
def leftshift_by2(x):
       return x[2:] + x[0:2]

# chuyen doi bit sang hexa
def bit_to_hexa(a):
    bits_4 = ''
    kq = []
    str_hexa = ''
    for i in range(0, len(a)):
        bits_4 = bits_4+str(a[i])
        if len(bits_4) == 4:
            kq.append(bits_4)
            bits_4 = ''
    for i in kq:
        for j in range(0, 16):
            if i == hexa[j]:
                str_hexa = str_hexa + str(text_hexa[j])
    return str_hexa

# dich key
def key_formation(leftbits, rightbits):
    rounds = 16
    count = 0
    while rounds != 0:
        count += 1

        if count in shift_pos:
            leftone = leftshift_by1(leftbits)
            rightone = leftshift_by1(rightbits)
        else:
            leftone = leftshift_by2(leftbits)
            rightone = leftshift_by2(rightbits)
        # gop bit
        combine_bits = leftone + rightone
        leftbits = leftone
        rightbits = rightone
        subkey = []
        for i in pc2:
            subkey.append(combine_bits[i-1])
        sub_keys.append(subkey)
        rounds -= 1

def key_generation():
    key = input("nhap key: ")
    # chuyen key ve nhij phan
    keybin = hextobin(key)
    key_length = len(keybin)
    if key_length < 64:
        while len(keybin) != 64:
            keybin = keybin + '0'
    keypc1 = pc1conversion(keybin)
    leftbits = keypc1[0:28]
    rightbits = keypc1[28:]
    key_formation(leftbits, rightbits)
    for i in range(0, len(sub_keys)):
        print('key round '+ str(i + 1)+ ': ' + str(bit_to_hexa(sub_keys[i])))

# hoan vi text dua tren ip
def ip_conversion(plain_text_bin):
    keylist = []
    for i in plain_text_bin:
        keylist.append(int(i))
    new_list = []
    for i in ip:
        new_list.append(keylist[i-1])
    return new_list

# ham tang kich thuoc bit tu 32 len 48 bit
def expansion_box(plain_right):
    new_list = []
    for i in ep:
        new_list.append(plain_right[i-1])
    return new_list

def check_xor_key(plain_exp, sub_key):
    plain_xor_list = []
    for i in range(0, len(plain_exp)):
        if plain_exp[i] == sub_keys[sub_key][i]:
            plain_xor_list.append(0)
        else:
            plain_xor_list.append(1)
    # sub_key += 1
    return plain_xor_list

# dua cac bit vao 8 Sbox
def plain_substution(plain_xor):
    plain_sub_list = []
    plain_list = []
    plain_xlist = []
    row = ""
    col = ""
    count = 0
    for i in range(0, len(plain_xor), 6):
        value = plain_xor[i:i+6]
        plain_sub_list.append(value)
    for word in plain_sub_list:
        row = str(word[0]) + str(word[-1])
        col = str(word[1]) + str(word[2]) + str(word[3]) + str(word[4])
        if count == 0:
            val = s0[s_rows.index(row)][s_cols.index(col)]
            plain_list.append(s_cols[val])
        if count == 1:
            val = s1[s_rows.index(row)][s_cols.index(col)]
            plain_list.append(s_cols[val])
        if count == 2:
            val = s2[s_rows.index(row)][s_cols.index(col)]
            plain_list.append(s_cols[val])
        if count == 3:
            val = s3[s_rows.index(row)][s_cols.index(col)]
            plain_list.append(s_cols[val])
        if count == 4:
            val = s4[s_rows.index(row)][s_cols.index(col)]
            plain_list.append(s_cols[val])
        if count == 5:
            val = s5[s_rows.index(row)][s_cols.index(col)]
            plain_list.append(s_cols[val])
        if count == 6:
            val = s6[s_rows.index(row)][s_cols.index(col)]
            plain_list.append(s_cols[val])
        if count == 7:
            val = s7[s_rows.index(row)][s_cols.index(col)]
            plain_list.append(s_cols[val])
        count += 1
    for i in plain_list:
        for j in i:
            plain_xlist.append(int(j))
    return plain_xlist

# doi chieu ma tran p
def plain_pbox(plain_sub):
    plain_p_text = []
    for i in p:
        plain_p_text.append(plain_sub[i - 1])
    return plain_p_text

def check_xor_left(plain_left, plain_p):
    plain_right_text = []
    for i in range(0, len(plain_left)):
        if plain_left[i] == plain_p[i]:
            plain_right_text.append(0)
        else:
            plain_right_text.append(1)
    return plain_right_text

def plain_ip_1(round_plain_text):
    cipher_text_bin = []
    for i in ip_1:
        cipher_text_bin.append(round_plain_text[i-1])
    return cipher_text_bin


def plain_text():
    plain_text = input('Nhap plain text: ')
    plain_text_bin = hextobin(plain_text)
    # print(plain_text_bin)
    plain_text_length = len(plain_text_bin)
    if plain_text_length < 64:
        while len(plain_text_bin) != 64:
            plain_text_bin += '0'
    plain_ip = ip_conversion(plain_text_bin)
    plain_left = plain_ip[0:32]
    plain_right = plain_ip[32:]
    rounds = 16
    sub_key = 0
    # khoi F
    while rounds != 0:
        plain_exp = expansion_box(plain_right)
        plain_xor = check_xor_key(plain_exp, sub_key)
        plain_sub = plain_substution(plain_xor)
        plain_p = plain_pbox(plain_sub)
        right_part = check_xor_left(plain_left, plain_p)
        round_text.append(plain_right + right_part)
        plain_left = plain_right
        plain_right = right_part
        sub_key = sub_key + 1
        rounds -= 1
    # for i in range(0, len(round_text)):
    #     print('key round ' + str(i) + ': ' + str(bit_to_hexa(round_text[i])))
    last_bin = round_text[15]
    last_bin_left = last_bin[32:]
    last_bin_right = last_bin[0:32]
    last_round = last_bin_left + last_bin_right
    cipher_bin = plain_ip_1(last_round)
    print("Cipher text: ", bit_to_hexa(cipher_bin))

key_generation()
plain_text()