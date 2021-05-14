c = {1,24,56,8,9,64,47,99,12,31}
oddcount = 0
evencount = 0

for i in c:
    if i % 2 == 0:
        evencount += 1
    else:
        oddcount += 1

print('evencount is -->',evencount)
print('oddcount is -->',oddcount)



