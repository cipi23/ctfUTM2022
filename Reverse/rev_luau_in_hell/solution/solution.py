enc = [40, 51, 35, 114, 60, 50, 127, 6, 111, 2, 65, 57, 96, 18, 48, 101, 25, 20, 71, 92, 73, 116, 1, 23, 0, 23, 1]
key = list(b"UTMCTF 2022")

for i in range(len(enc)):
    enc[i] ^= key[i % len(key)]

for i in range(len(enc)-1, -1, -1):
    for j in range(len(enc)-1, i, -1):
        enc[i], enc[j] = enc[j], enc[i]

flag = ''
for c in enc:
    flag += chr(c)
print(flag)