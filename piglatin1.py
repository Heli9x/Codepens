alpha = list(map(chr, range(97, 123)))
vowels = ['a', 'e', 'i', 'o', 'u']

def latinize(word):
    firstCon = []
    letters = list(word)
    for letter in letters:
        if letter in vowels:
            if letters.index(letter) == 0:
                return word
            else:
                break
        else:
            firstCon.append(letter)

    for letter in firstCon:
        letters.remove(letter)
        letters.append(letter)
    
    letters.append('ay')
    latinized = ''
    for letter in letters:
        latinized += letter
    
    return latinized

print(latinize('Friday'))