from Crypto.Util.number import bytes_to_long, long_to_bytes

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_KEY1_KEY3_KEY2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"


KEY1 = bytes_to_long(bytes.fromhex(KEY1))
KEY2_KEY1 = bytes_to_long(bytes.fromhex(KEY2_KEY1))
KEY2_KEY3 =  bytes_to_long(bytes.fromhex(KEY2_KEY3))
FLAG_KEY1_KEY3_KEY2 = bytes_to_long(bytes.fromhex(FLAG_KEY1_KEY3_KEY2))

KEY2 = KEY2_KEY1 ^ KEY1
KEY3 = KEY2_KEY3 ^ KEY2
FLAG = FLAG_KEY1_KEY3_KEY2 ^ KEY3 ^ KEY2 ^ KEY1

print(long_to_bytes(FLAG))