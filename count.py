import json


find = 'SUM_OHEAD_WTX_BYTES'
with open("/home/rshetty/basic/formatted.json", "r") as f:
    data = f.read()
    total = data.count(find)
    print(total)


