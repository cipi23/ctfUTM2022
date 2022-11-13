import sequtils, strutils, strformat

# Reads string from file
var f = open("flag.txt", fmRead).readAll()
var xor_key = uint8(0xff)
var char_list = toSeq(f.items)
echo fmt"Current flag: {f}"
echo fmt"XOR key: {xor_key}"
echo char_list.map do (c: char) -> char:
    char(uint8(c).xor(uint8(xor_key)))
