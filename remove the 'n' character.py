#adding some title 
print('\nREMOVING THE FIRST n IN THE WORD.\n')

#you can type any word here
word = input('TYPE THE WORD YOU WANT:')

#this function remove the character in the word you type
def remove(word, number):
    print('\nOriginal Word :', word)
    cancel = word [number:]
    print('\nResult:')
    return cancel

#defines how many should the function remove in the word you type
print(remove(word, 2))
print(remove(word, 7))