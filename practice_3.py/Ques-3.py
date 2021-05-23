nest_list = []
print('enter values seperated by commas')
while True:
    items = input('enter values >> ').split(',')
    if len(items)>1  and items[0] !='':
        nest_list.append(items)
    else:
        break
print(nest_list)