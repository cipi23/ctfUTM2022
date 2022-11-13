# Solutions for Hacker's Library

* The technique that is being abused is called Hash Length Extension.
* ALl of the needed information in order to recognize it is given to you in the __What is it?__ menu. 

In order to exploit it, use the *hashpumpy* module for Python.

If you are using Python 3.10 it won't work because the __DeprecationWarning__ has been ignored for way too long.
In this case, you can compile the tool from this repository : https://github.com/bwall/HashPump and spoof the hash manually.

```txt
Flag: 
UTM{3xt3nd1ng_th3_sc0pe}
```
