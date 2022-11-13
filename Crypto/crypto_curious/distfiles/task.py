from Crypto.Util.number import getPrime
import os

flag = os.getenv("FLAG", "UTM{that's_what_i_call_beginner_friendly}")
m = int(flag.encode().hex(), 16)

p = getPrime(512)
q = getPrime(512)

n = p*q

print("n =", n)
print("a =", pow(m, p, n))
print("b =", pow(m, q, n))
print("c =", pow(m, n, n))
