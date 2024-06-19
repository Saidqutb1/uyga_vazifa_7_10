#1 Slice the middle of a list backwards

def reverse_middle(lst):
    l = len(lst)//2 - 1
    return lst[l:-l][::-1]


#2 Parts of a list

def partlist(arr):
    result = []
    for i in range(1, len(arr)):
        result.append((' '.join(arr[:i]), ' '.join(arr[i:])))
    return result


#3 ORing arrays

from itertools import zip_longest

def or_arrays(a1, a2, d=0):
    return [x|y for x,y in zip_longest(a1, a2, fillvalue=d)]


#4 Remove the minimum

def remove_smallest(numbers):
    if not numbers:
        return []
    min_val = min(numbers)
    for i in range(len(numbers)):
        if numbers[i] == min_val:
            return numbers[:i] + numbers[i+1:]


#5 Offspring Traits

def bear_fur(bears):
    fur_combinations = {
        ('black', 'black'): 'black',
        ('brown', 'brown'): 'brown',
        ('white', 'white'): 'white',
        ('black', 'brown'): 'dark brown',
        ('brown', 'black'): 'dark brown',
        ('black', 'white'): 'grey',
        ('white', 'black'): 'grey',
        ('brown', 'white'): 'light brown',
        ('white', 'brown'): 'light brown'
    }
    sorted_bears = tuple(sorted(bears))
    return fur_combinations.get(sorted_bears, 'unknown')
