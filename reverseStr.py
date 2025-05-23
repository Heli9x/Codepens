# road = daor

'''
In order to reverse a string in python and make our code reusable,
define a function. In that function you'll have a parameter taking in a string,

two variables, one containing a split-word list and the other a reversed string of letters 
of the given string,

a loop, in this loop we'll iterate by the value of the length of the split-word list and in each iteration
we'll add the index value of the length of the split-word list(len(splitWord)) minus the iteration number(i)
to the reversedWord making one reversed word.


and finaly our work is done. Enjoy your day.
'''

def reverseStr(data:str):
    splitWord = list(data)
    reversedWord = ''

    for i in range(len(splitWord)):
        reversedWord += splitWord[(len(splitWord)-1)-i]
        
    
    return reversedWord


'''
#example

def Run():
    word = 'Monopoly'
    print(reverseStr(word))
    
Run()
'''
