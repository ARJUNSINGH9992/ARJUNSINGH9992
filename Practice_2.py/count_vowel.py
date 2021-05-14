string = 'electric vehicles are the future '
count = 0
vowel = 'aeiou'
for i in string:
    if i in vowel:
        count += 1
print('The vowel count is',count)
print(string)
