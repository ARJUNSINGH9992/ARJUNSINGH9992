num = 1000
l = 1

for x in range(1,num):
    if l == 50:
        break
    else:
        for i in range(2,x):
            if(x % i == 0):
                break
            print(x,end = ' ')
            l += 1
