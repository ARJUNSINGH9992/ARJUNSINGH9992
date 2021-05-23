cricketers = []
while True:
    name = input('cricketers name: ')
    if not name:
        break
    elif name[0].isupper():
        cricketers.append(name)
print(cricketers)