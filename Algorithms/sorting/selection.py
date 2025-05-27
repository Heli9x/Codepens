#selecton sorting

'''
When dealing with a sorting algorithm like a the 
selection sort, there's a thin line between easy
and confusing. However you got on the right bus
at the right station. Today we'll go through the 
steps towards achieving a good and basic selection sort
algorithm.

Okay first thing we want to know is that a selection sort
algorithm starts with first element assuming its the smallest.
Always remember to work with index values, its better that way.
Then compares it to all other elements to see if it is.
for example in the first iteration of the nested loop, 
the algorithm will take index y value and compare it with smallest value index, 
and if the current index value(y) is smaller than the smallest index value,
then the algorithm will set y index as the smallest value index, 
and in the case that y is not, the algorithm will continue to the next index. 
Now the thing about the selection sort is that, when the iteration number of
the first loop increases the iterations of the second loop shortens.
So for example if the first loop is on the 5th iteration and the
length of the list is 9, the nested loop will only iterate in the of range(5+1, 9)
which means it only iterates 3 times in the 5th phase.

Anyway with all that explained, we move on to the practical part.
To begin, we'll create a variable storing our unsorted list,
next we create a loop based on the length of the unsorted list,
within the loop define a minimum index variable to store the smallest value index.

Now within the loop, create another for loop iterating between the current 
iteration number of the first loop + 1 and the length of the unsorted list.
in this loop we'll set a condition to determine if the current index value
is less than the minimun index value. If that is the case then we'll set 
the minimun index to the current index.

After that, at the end of the nested loop, we'll swap the values of the
minimum index(min_index) and the index determined by the first loop(x).

And finally print out the sorted list.

'''

nums = [4,1,5,3,2,9,7]

for x in range(len(nums)):
    min_index = x
    for y in range(x+1, len(nums)):
        if nums[y] < nums[min_index]:
            min_index = y
    
    nums[x], nums[min_index] = nums[min_index], nums[x] 

print(nums)