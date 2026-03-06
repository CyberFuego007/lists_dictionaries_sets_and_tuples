import random
import string

#use the python module random and the function randint() to create a list of 1000 random integers
random_numbers = []
for i in range(1000):
    random_numbers.append(random.randint(1,100))

print("Step 1: List of 1000 random integers:")
print(random_numbers)

#use len(), count(), sum(), and sort() functions on this list.  use some sort of print statement to show me the values, and use comments to tell me what each function does.
#len(list) returns how many are in list
print("\nStep 2: Using len()")
print("len(random_numbers) =",len(random_numbers))

#count(value) returns how many times a set value appears in the list
#number 77 is chosen
print("\nStep 2: Using count()")
print("random_numbers.count(77) =", random_numbers.count(77))

#sum() is the sum of all values in list
print("\nStep 2: Using sum()")
print("sum(random_numbers) =", sum(random_numbers))

#sort() sorts list in order in place
print("\nStep 2: Using sort()")
random_numbers.sort()  #I forgot the () and had trouble finding out why it would not sort
print("Sorted List:")
print(random_numbers)

#gettysburg step 4


#create a set of unique numbers from your list of numbers used in step 2
#set(list) takes list into set and removes the duplicates
number_set=set(random_numbers)
print("\nStep 6: Use Set of Unique numbers on list")
print(number_set)

#Sets are distinctly different data structures from lists.  They are both iterable so behave in many of the same ways.
#There is a simple way to convert a set into a list.  do this in your code and use a comment to point out this conversion
number_list=list(number_set)
print("\nStep 7: Set converted into a list:")
print(number_list)
