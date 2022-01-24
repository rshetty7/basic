


x = [

[0, 1, 1, 0, 0],

[0, 1, 1, 0, 1],

[0, 1, 0, 0, 0],

[0, 0, 0, 0, 0],

[1, 1, 1, 0, 0],

]

count = 0
for a in x:
    count+=a.count(1)
print(count)
