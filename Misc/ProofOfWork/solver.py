#!/usr/bin/env python3
from pwn import * 
from base64 import b64decode
from tqdm import tqdm

r = remote("34.78.240.11", 65124)
for _ in tqdm(range(1500)):
    r.recvuntil(b"TODO : ")
    work = r.recvline().strip()
    r.recv()
    answer = b64decode(work)
    r.sendline(answer)
flag = r.recv().decode()
print(flag)
