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
    for i in range(len(s)):
        if s[i] == 'a':
            if ((i+1 < len(s) and s[i +1] == 'z') or
                (i+2 < len(s) and s[i+2] == 'z') or
                (i+3 < len(s) and s[i+3] == 'z')):
                     return True
    return False

print nearby_az('jennisapizza')
print nearby_az('jhileneissosmart')


# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.

def sum_list(y):
    x = 0
    for i in y:
        x = x + i
    return x


print sum_list([2,7,9])

# Write a method that takes an array of numbers. If a pair of numbers
# in the array sums to zero, return the positions of those two numbers.
# If no pair of numbers sums to zero, return None.

import itertools
def position(q):
    result =[]
    w = itertools.combinations(q,2)
    for k in w:
        if k[0] + k[1] == 0:
            result.append((q.index(k[0]), q.index(k[1])))
            #without appending to empty list and returning
            #only the first tuple that equals 1 will be returned
            #return q.index(k[0]), q.index(k[1])

    if result == []:
        return None
    return result

print position([1, 2,3,-1,4,0, -4])
print position([1, 2,3,0, -4])

# Write a method that takes in a number and returns true if it is a
# power of 2. Otherwise, return false.
# You may want to use the `%` modulo operation. `5 % 2` returns the
# remainder when dividing 5 by 2; therefore, `5 % 2 == 1`. In the case
# of `6 % 2`, since 2 evenly divides 6 with no remainder, `6 % 2 == 0`.

def divisible(t):
        if t % 2 == 0:
            return True
        else:
            return False

print divisible(890)
print divisible(10)
print divisible(33)

#Create a function that takes an array and separates numbers that are odd and
#those that are even.


def evenorodd(thing):
    even = []
    odd = []
    for i in thing:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print odd
    print even

evenorodd([1,2,3,4,5,6,7,8,9,99,23,43,44,17])

# Write a method that takes an array of numbers in. Your method should
# return the third greatest number in the array. You may assume that
# the array has at least three numbers in it.

def third_greatest(r):
    #range(3), max
    #sort, [-3]
    biggest = r[0]
    time = r[:]
    big = []
    for _ in range(2):
        biggest = time[0] #thank's Jen! & Ryan
        for i in time:
            if i > biggest:
                biggest = i
        time.remove(biggest)
    biggest = time[0]
    for i in time:
        if i > biggest:
            biggest = i
    return biggest

print third_greatest([100, 156, 23, 45, 94])
print third_greatest([17,22,84,56,78])
print third_greatest([17,22,84,56,23,78,100, 156])

 # Write a method that takes in a string. Your method should return the
 # most common letter in the string, and a count of how many times it
 # appears. Then iterate a list after.

 def duplicate(w):
     dict = {}
     for i in w:
         if i not in dict:
             dict[i] = 0
         dict[i] = dict[i] + 1
     if dict[i] == 1:
         return None
     maxi= max(dict, key= dict.get)
     return maxi, dict[maxi]
      #v=list(d.values())
      #k=list(d.keys())
      #return k[v.index(max(v))]

 print duplicate('abcdcbbb')
 print duplicate('hkls')
 print duplicate('there once was a young boy who owned a nice toy but')
 #strip all white spaces

#Convert Roman Numerals to Integers

# Cracking the code in Python

#Implement an algorithm to determine if a string has all unique characters
