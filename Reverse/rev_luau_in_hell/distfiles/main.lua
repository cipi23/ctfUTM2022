local libflag = require "libflag"
io.write("FLAG: ")
flag = io.read("*l")
if libflag.checkFlag(flag, "UTMCTF 2022") then
   print("Correct!")
else
   print("Wrong...")
end