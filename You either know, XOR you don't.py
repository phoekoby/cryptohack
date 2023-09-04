from Crypto.Util.number import bytes_to_long, long_to_bytes
import string
inp = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

inp_bytes = bytes.fromhex(inp)
key = b'myXORkey'
result = ''
for i in range(0, len(inp_bytes)):
    result += chr(inp_bytes[i] ^ key[i % len(key)])
print(result)
