x = [
[0, 1, 1, 0, 0],
[0, 1, 1, 0, 1],
[0, 1, 0, 0, 0],
[0, 0, 0, 0, 0],
[1, 1, 1, 0, 0],
]

total=0
for a in x:
    for i in a:
        if i ==1:
            total+=1
print(total)



#count = 0
#for a in x:
#count+=a.count(1)
#print(count)

