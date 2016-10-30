# Prep Work
# Write a method that will take a string as input, and return a new
# string with the same letters in reverse order.
def reverse(string):
    string = string[::-1]
    return string

# OR

def reverse2(string):
    string = string.split()
    string2 = string[::-1]
    string3 = ' '.join(string2)
    return string3

print reverse("I like eggs")
print reverse2("I like eggs")

# Write a method that takes an integer `n` in; it should return
# n*(n-1)*(n-2)*...*2*1. Assume n >= 0.

def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        print "Not Valid. Number must be larger than 0."
    else:
        return n * factorial(n-1)

print factorial(4)

# Write a method that takes in a string. Return the longest word in
# the string. You may assume that the string contains only letters and
# spaces.
#
# You may use the String `split` method to aid you in your quest.

def longest_word(sentence):
    sentence = max(sentence.split(), key = len)
    return sentence

print longest_word("Ay yo ma, where you at?")

# Write a method that takes in an integer `num` and returns the sum of
# all integers between zero and num, up to and including `num`.
# Two ways! Thanks Stack Overflow
def sum_nums(num):
    total = 0
    for i in range(num + 1):
        total += i
    print total

    #OR

def sum_numbers(num):
    return sum(range(num +1))
#Explained Example: num = 5
# range(num) = [0,1,2,3,4]
# range(num + 1) = [0,1,2,3,4,5]
#sum([0,1,2,3,4,5]) adds them all together
# Thanks Stack Overflow

print sum_nums(5)
print sum_nums(2)
print sum_numbers(5)
print sum_numbers(2)

# Write a method that will take in a number of minutes, and returns a
# string that formats the number into `hours:minutes`.
def time_conversion(min):
    minutes = min
    hour = minutes / 60
    left = minutes % 60
    print "%d:%d" % (hour, left)

time_conversion(70)
time_conversion(170)

# Write a method that takes a string and returns the number of vowels
# in the string. You may assume that all the letters are lower cased.

def count_vowels(s):
    vowel_count = 0
    for i in s:
        if i in "aeiouAEIOU":
            vowel_count += 1
    return vowel_count

print count_vowels("pizza please")
print count_vowels("Do you love me?")

# Write a method that takes a string and returns true if it is a
# palindrome. A palindrome is a string that is the same whether written
# backward or forward. Assume that there are no spaces; only lowercase
# letters will be given.

def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

print palindrome("racecar")
print palindrome("pizza")

# Write a method that takes a string in and returns true if the letter
# "z" appears within three letters **after** an "a". You may assume
# that the string contains only lowercase letters.

def nearby_az(s):



# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.

def sum_list(ay):
    x = 0
    for i in ay:
        x = x + i
    return x


print sum_list([2,7,9])




# Cracking the code in Python

#Implement an algorithm to determine if a string has all unique characters
