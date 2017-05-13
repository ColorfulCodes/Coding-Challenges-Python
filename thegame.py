#The game:feed each challenges into a variable then initiate Random
#include skip option. Place every 5 in batches. Have option to select batch.
import random, os
from time import sleep

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

nearby_az = """Write a method that takes a string and returns true if it is a
palindrome. A palindrome is a string that is the same whether written
backward or forward. Assume that there are no spaces; only lowercase
letters will be given."""

palindrome = """Write a method that takes a string in and returns true if the letter
"z" appears within three letters **after** an "a". You may assume
that the string contains only lowercase letters."""

sum_list = """Define a procedure, sum_list, that takes as its input a
list of numbers, and returns the sum of all the elements in the input list."""

position = """Write a method that takes an array of numbers. If a pair of numbers
in the array sums to zero, return the positions of those two numbers.
If no pair of numbers sums to zero, return None."""

divisible = """Write a method that takes in a number and returns true if it is a
power of 2. Otherwise, return false. You may want to use the `%` modulo operation. `5 % 2` returns the
remainder when dividing 5 by 2; therefore, `5 % 2 == 1`. In the case
of `6 % 2`, since 2 evenly divides 6 with no remainder, `6 % 2 == 0`."""

evenorodd = """Create a function that takes an array and separates numbers that are odd and
#those that are even."""

third_greatest = """Write a method that takes an array of numbers in. Your method should
# return the third greatest number in the array. You may assume that
# the array has at least three numbers in it."""

duplicate = """Write a method that takes in a string. Your method should return the
most common letter in the string, and a count of how many times it
appears. Then iterate a list after."""

dashes = """Write a method that takes in a number and returns a string, placing
a single dash before and after each odd digit. There is one
exception: don't start or end the string with a dash."""

capitalize = """Write a method that takes in a string of lowercase letters and
spaces, producing a new string that capitalizes the first letter of
each word. You'll want to use the `split` and `join` methods. Also, the String
method `upcase`, which converts a string to all upper case will be
helpful."""

uhh = """ Write a method that takes in a string and an array of indices in the
# string. Produce a new string, which contains letters from the input
# string in the order specified by the indices of the array of indices.
"""

prime = """ Write a method that takes in an integer (greater than one) and
returns true if it is prime; otherwise return false."""

nth_prime = """ Write a method that returns the `n`th prime number. Recall that only
# numbers greater than 1 can be prime. No positive dividers other than
#one and itself"""

bprime = """List all prime numbers between this and this."""
# most common sites people visit, average person's day


batch1 = [reverse, reverse2, factorial, longest_word, sum_nums, time, vowels]

batch2 = [palindrome, nearby_az, sum_list, position, divisible, evenorodd, third_greatest]

batch3 = [duplicate, dashes, capitalize, uhh, prime, nth_prime, bprime]

def answer():
    print "\n"
    answer = raw_input("Great Choice! When finished type 'n' to move to next question or 'e' to exit: ")
    if answer == "n":
        print random.choice(batch1)
        os.system('clear')
    elif answer == "e":
        return

def test():
    emp = []
    os.system('clear')
    print "Welcome to interview prep. You will be working through your chosen batch. \n"
    choice = raw_input( "Which batch would you like? Batch 1, 2, or 3? ")
    if choice == '1':
        os.system('clear')
        print random.choice(batch1)
        answer()

    elif choice == '2':
        os.system('clear')
        print random.choice(batch2)
        answer()

    elif choice == '3':
        os.system('clear')
        print random.choice(batch3)
        answer()

    else:
        os.system('clear')
        print "Sorry, not an option. Please try again."
        sleep(3)
        test()
    #next question option, store in array when next is continued. Then state
    #current batch is complete
    #emp.append(i)




test()
