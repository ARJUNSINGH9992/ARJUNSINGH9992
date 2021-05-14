string = 'arjun is greatest of all times'
vowel = ['a','e','i','o','u']
for i in string:
    if i in vowel:
        string = string.replace(i,"")
print(string)