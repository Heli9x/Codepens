#alphabet pig latin


'''
Pig Latin.py

Coding a pig latin program.

first we'll begin with a list of the alphabetical letters of english and create a list of vowels
In the first stage we'll work on converting a word to pig latin.

Latinize the word

Now we create a function taking in any through a parameter,
create an empty list that will hold the first consonants of a word once we break it.
oh yeah we'll need to break the word into a list in order to achieve our goal.

Next, create a list variable containing each letter of the word as an element.
With the word listified, we'll loop through the letters. 

Create a 'for loop' looping through each letter and in the loop,
set a conditional statement to determine if the letter on iteration is a vowel or not
using our vowel list.

Within the if statement create another if(nested if) to decide on whether that vowel is 
the first letter of the word. In the case that it is, return the word as it is.

In the else(nested else) break the loop. Why? because this shows that we bumped into a 
vowel of the word which is an end road for us.

In the else statement of the unested condtional statement, append the letter to the 'first consonant' list.

after that create another 'for loop', in this loop using the 'first consonant' list elements
we'll move the first consonants and add the back to the end of the letters by removing them and
appending them.

In the next step away from the loop we add 'ay' to the letters list and create a string variable
to hold the latinized word.

And now to completely model the word back together, we'll loop through each element in the letters list
and add it to the latinized word string.

Finally, we return the word as a string and our function is done.

At this point this seems like loads of work for a fun challenge but hang on 
we just finished the main part. So the good news is that you're almost done.

Okay so our goal is to pig-latinize an entire sentence, so we'll have to now 
create two functions, one seperating the words in to each a list and the other
taking the seperated word list, latinizing each word and finally outputing the final
result.

Break Sentennce

For this function, we're taking in a sentence and simply turn each word
into an element of a list by splitting the string.


Latinize Sentence

Finally at the conclusion. Lets get right into it and out.
Okay in this function, we'll take in a whole sentence through a paramenter, 
then create a list variable containing each word of that sentence as a list elemnet.
Now we create a string variable to contain the latinized sentence.

Then for the last touches we add each word(immediately after latinizing it) to the 
latinized sentence string and after every addition to the string we add a space.

and for the conclusion, we return the latinized sentence.

'''

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

def breakSen(sentence):
    sentence = sentence.split(' ')
    return sentence

def latinizeSen(sentence):
    sentence = breakSen(sentence)
    latinSen = ''
    for word in sentence:
        latinSen += latinize(word)
        latinSen += ' '

    return latinSen


print(latinizeSen('Today is Friday'))