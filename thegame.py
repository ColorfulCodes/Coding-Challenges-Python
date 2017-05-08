#The game:feed each challenges into a variable then initiate Random
#include skip option. Place every 5 in batches. Have option to select batch.
import random, os

reverse = "Write a method that will take a string as input, and return a new string with the same letters in reverse order.\n"
reverse2 = "Reverse string input with recursion\n"

factorial = "Write a method that takes an integer `n` in; it should return n*(n-1)*(n-2)*...*2*1. Assume n >= 0.\n"
longest_word = ''' Write a method that takes in a string. Return the longest word in
the string. You may assume that the string contains only letters and
spaces. You may use the String `split` method to aid you in your quest.\n'''

sum_nums = """Write a method that takes in an integer `num` and returns the sum of
all integers between zero and num, up to and including `num`. Two ways! Thanks Stack Overflow\n"""

time = """Write a method that will take in a number of minutes, and returns a
string that formats the number into `hours:minutes`.\n"""

vowels = """Write a method that takes a string and returns the number of vowels
in the string. You may assume that all the letters are lower cased."""

batch1 = [reverse, reverse2, factorial, longest_word, sum_nums, time, vowels]
batch2 = []

def test():
    emp = []
    os.system('clear')
    print "Welcome to interview prep. You will be working through batch 1. \n"
    #next question option, store in array when next is continued. Then state
    #current batch is complete
    os.system('clear')
    print random.choice(batch1)
    #emp.append(i)
    answer = raw_input("When finished type 'n' to move to next question or 'e' to exit: ")
    if answer == "n":
        print random.choice(batch1)
        return test()
    elif answer == "e":
        return



test()
