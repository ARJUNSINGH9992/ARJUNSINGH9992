names = ['Ritesh Kumar Sharma','Vivek Sharma','pope','elex','elin']
names_without_a_or_o = [name for name in names if ('a' not in name.lower() and 'o' not in name.lower())]
print(names_without_a_or_o)