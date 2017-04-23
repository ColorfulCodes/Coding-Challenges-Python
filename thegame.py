#The game:feed each challenges into a variable then initiate Random
#include skip option. Place every 5 in batches. Have option to select batch.
import random, os

reverse = "Write a method that will take a string as input, and return a new string with the same letters in reverse order."
reverse2 = "reverse string input with recursion"

factorial = " Write a method that takes an integer `n` in; it should return n*(n-1)*(n-2)*...*2*1. Assume n >= 0."
longest_word = ''' Write a method that takes in a string. Return the longest word in
the string. You may assume that the string contains only letters and
spaces. You may use the String `split` method to aid you in your quest./n'''

add = """ Write a method that takes in an integer `num` and returns the sum of
all integers between zero and num, up to and including `num`. Two ways! Thanks Stack Overflow"""

words = [reverse, reverse2, factorial, longest_word, add]
def test():
    os.system('clear')
    print random.choice(words)
    os.linesep

test()
