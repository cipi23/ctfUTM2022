from Crypto.Util.number import inverse

key, c = open("distfiles/output.txt").read().strip().split("\n")

s, t, n = eval(key)
c = eval(c)

flag = []
for i in c:
    c1 = i[0]
    c2 = i[1]
    psmt = c1 * pow(c2, -1, n) % n
    for m in range(1, 256):
        rs = c1 * pow(m, -1, n) % n
        if pow(psmt, s, n) == pow(rs, s-t, n):
            flag.append(chr(m))
            print(chr(m), end='', flush=True)

