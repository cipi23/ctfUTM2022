import sequtils, strutils
echo if stdin.readLine == (@['\xAA', '\xAB', '\xB2', '\x84', '\x91', '\xCE', '\x92', '\xA0', '\xCE', '\x8C', '\xA0', '\x94', '\xCE', '\x91', '\x9B', '\xCB', '\xA0', '\x9C', '\xCF', '\xCF', '\x93', '\x82'].map do (c:char) -> char: char(uint8(c).xor(0xff))).join(""):
  "Submit the flag! FAST!"
else:
  "That's not it..."
