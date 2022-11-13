from Crypto.Util.number import getPrime, getRandomRange, inverse, GCD
import os

flag = os.getenv("FLAG", "UTM{flag_placeholder}").encode()


def generateKey():
    p = getPrime(512)
    q = getPrime(512)

    n = p * q
    phi = (p-1)*(q-1)

    while True:
        a = getRandomRange(0, phi)
        b = phi + 1 - a

        s = getRandomRange(0, phi)
        t = -s*a * inverse(b, phi) % phi

        if GCD(b, phi) == 1:
            return (s, t, n), (a, b, n)


def encrypt(m, k):
    s, t, n = k
    r = getRandomRange(0, n)
    return m * pow(r, s, n) % n, m * pow(r, t, n) % n


def decrypt(c1, c2, k):
    a, b, n = k
    return pow(c1, a, n) * pow(c2, b, n) % n


publicKey, privateKey = generateKey()

c = []
for m in flag:
    c1, c2 = encrypt(m, publicKey)
    assert decrypt(c1, c2, privateKey)

    c.append((c1, c2))

print(publicKey)
print(c)

