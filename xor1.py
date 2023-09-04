s = "label".encode('utf-8')
res = []
for byt in s:
    res.append(byt ^ 13)

print(''.join([chr(x) for x in res]))
