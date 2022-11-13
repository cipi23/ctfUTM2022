flag = list(b"UTMCTF{lu4_1s_4ls0_4_th1ng}")
key = list(b"UTMCTF 2022")

for i in range(len(flag)):
    for j in range(i+1, len(flag)):
        flag[i], flag[j] = flag[j], flag[i]

for i in range(len(flag)):
    flag[i] ^= key[i % len(key)]

print(flag)