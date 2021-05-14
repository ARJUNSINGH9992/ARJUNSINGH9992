word = input('enter your word: ')

if len(word) >0:
    print(word,len(word))

for i in range(len(word)-1,-1,-1):
    print(word[i],end='')

# reverse word in python is actually
# word[::-1]
