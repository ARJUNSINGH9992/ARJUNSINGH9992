a = 0
b = 1
print(a,b,end=' ')
for i in range(50):
    c = a + b
    if c > 50:
        break
    print(c,end=' ')
    a = b
    b = c