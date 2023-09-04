from Crypto.Util.number import bytes_to_long, long_to_bytes

inp = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
inp = bytes.fromhex(inp)

for i in range(256):
    res = b''
    for b in inp:
      res_b = b ^ i
      res += long_to_bytes(res_b)
    try:
        res = res.decode('utf-8')
        # print(res)
        if "crypto" in res:
            print(i, res)
            break
    except Exception as e:
        continue