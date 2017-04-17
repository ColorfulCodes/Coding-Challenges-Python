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

#reverse with recursion
def reverse(s):
    print s
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]


print reverse("hola")
print reverse("timeline")

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

 # Write a method that takes in a number and returns a string, placing
 # a single dash before and after each odd digit. There is one
 # exception: don't start or end the string with a dash.

 def dashes(s):
     res = ''
     for i, x in enumerate(s):
         if int(x) % 2 != 0:
             if i == 0:
                 res += x + '-'
             elif i == len(s) - 1:
                 res += '-' + x
             else:
                 res += '-' + x + '-'
         else:
             res += x
     return res

 print dashes('0802341')
 print dashes('123456789011')
 print dashes('84375495947336485')


 # Write a method that takes in a string of lowercase letters and
 # spaces, producing a new string that capitalizes the first letter of
 # each word.
 # You'll want to use the `split` and `join` methods. Also, the String
 # method `upcase`, which converts a string to all upper case will be
 # helpful.

 def capitalize(s):
     #split every word
     #s.split(' ')
     #capitalize first letter of each word
     s = s.split()
     answer = []
     for i in s:
         i = i[0].upper() + i[1:]
         answer.append(i)
         t = " ".join(answer)
     return t
     #lst = [word[0].upper() + word[1:] for word in s.split()]
     #s = " ".join(lst)


 print capitalize('there was once a time of love')
 print capitalize('pina colada')


# Write a method that takes in a string and an array of indices in the
# string. Produce a new string, which contains letters from the input
# string in the order specified by the indices of the array of indices.

def uhh(y,x):
    #count indices in string
    pizza = ''
    for i in range(len(y)):
        pizza += y[x[i]]
    return pizza


print uhh('word', [3,2,3,2])
#output  --> drdr
print uhh('umbrella', [3,2,5,6,7,4,3,2])
print uhh('jamba', [4,1,3,3,1,2])

# Write a method that takes in an integer (greater than one) and
# returns true if it is prime; otherwise return false.
def prime(x):
    if x >= 2 :
        for i in range(2,x):
            #print(x % i)
            #print(x, i)
            if x % i == 0:
                return False
            #if not (x % i):
                #return False
            return True
    else:
        return False

    #return True

print prime(6)
print prime(1)
print prime(13)
print prime(1000)

# Write a method that returns the `n`th prime number. Recall that only
# numbers greater than 1 can be prime. No positive dividers other than
#one and itself
def nth_prime(n):
    #print 'Choose any number between 2 and 1000.'
    emp = []
    i = 2
    l = 0
    while i < 1000:
        for l in range(2, i+1):
        #search range 2 to 3 and up
            if i % l == 0:
                #divisors less than i
                break
        if l == i and i != 2:
            emp.append(i)
        i = i + 1
    if emp:
        return emp[n-1]
    else:
        return None



print nth_prime(3)
print nth_prime(18)
print nth_prime(1)
print nth_prime(4)
print nth_prime(6)

#list all prime numbers between this and this.

def bprime(x,y):
    for i in range(x,y):
        prime = True
        for j in range(2, i):
            #range needs to start at 2 to check every number up to there
            if i < 2:
                print "Only numbers greater than one are accepted"
                return

            if i % j == 0:
                prime = False

        if prime:
            print i

bprime(10,14)

#check if word is a palindrome. Many ways.
#check if whether given string is a palindrome. Not returning true or false in terminal.
def is_palindrome(x):
    if x == x[::-1]:
        print x
        return True
    else:
        return False

is_palindrome("mom")
is_palindrome("teacher")
is_palindrome("madam")

#using with while loop
def is_palindrome(word):

    letters = list(word)
    is_palindrome = True
    i = 0

    while len(letters) > 0 and is_palindrome:
        if letters[0] != letters[(len(letters) - 1)]:
            is_palindrome = False
        else:
            letters.pop(0)
            if len(letters) > 0:
                letters.pop((len(letters) - 1))

    print is_palindrome

is_palindrome("mom")
is_palindrome("team")

# with a for-loop
def is_palindrome(word):

    letters = list(word)
    is_palindrome = True

    for letter in letters:
        if letter == letters[-1]:
            letters.pop(-1)
        else:
            is_palindrome = False
            break

    print is_palindrome


is_palindrome("mom")
is_palindrome("team")
is_palindrome("madam")

#Check whether a string is an integer or float

>>> x = 12
>>> isinstance(x, int)
True
>>> y = 12.0
>>> isinstance(y, float)
True

# OR

inNumber = somenumber
try:
    inNumberint = int(inNumber)
    print "this number is an int"
except ValueError:
    pass
try:
    inNumberfloat = float(inNumber)
    print "this number is a float"
except ValueError:
    pass

#Implement an algorithm to determine if a string has all unique characters
def unique(s):
    #s = list(s)
    #create list add unique characters for x in list. unique(x)
    if len(set(s)) == len(s):
        print True
    else:
        print False

# turn into set. Check if size of set is smaller than size of string.
# no sets: do hash table.

#with a hashmap
def unique(string):
    hashMap = {}
    for c in string:
        if c not in hashMap:
            #This is just a place holder to add c to dict. "None" can be anything
            # You could put a second if for last letter of word and not in hashMap
            #then add. But it is cleaner without another if.
            hashMap[c] = None
        elif c in hashMap:
            return False
    return True


print unique("food") # should print False
print unique("numbers") #should print True
print unique("greest") #False

#recursion is this
"""def fun(x):
    x+= 1
    if x <= 10:
        f(x)
    else:
        return x """

# Find wheter a substring is in another
def substring(x,y):
    if x in y:
        print True
    else:
        print False
substring("what","Hey girl whatcha up to")
substring("ayo","Hey girl whatcha up to")
substring("rl","Hey girl whatcha up to")

#OR
#This function returns -1 when there is no substring.

def sub(x,y):
    if x.find(y):
        print True
    else:
        print False
sub("I like eggs", "gg")


## Write a method that takes in a string of lowercase letters (no
# uppercase letters, no repeats). Consider the *substrings* of the
# string: consecutive sequences of letters contained inside the string.
# Find the longest such string of letters that is a palindrome.
# Note that the entire string may itself be a palindrome.
def lpalindrome(x):
    if x == x[::-1]:
        print "this is a palindrome"
        return True
    x = x.split()
    for i in x:
        if i == i[::-1]:
            #emp.append(i)
            #for i in emp:
            #if i <= range(i+1):
            print i


lpalindrome("sore was I ere I saw eros")
lpalindrome("I like eggs")
lpalindrome("radar")
lpalindrome("anna")

#check if a string has duplicates

def duplication(string):
    count = {}
    #string = string.split()
    for s in string:
      if count.has_key(s):
        count[s] += 1
      else:
        count[s] = 1

    #for key in count:
      #if count[key] > 1:
        #print key, count[key]

print duplication("I like eggs and popcorn iceiiiiiiii")
print duplication("recurse center is lit")


#check if a string has duplicates

def duplicates(string):
    count = []
    for c in string:
      if c not in count:
        count.append(c)
      else:
        return True
    return False


print duplicates("I like eggs")
print duplicates("recurse center is awesome")
print duplicates("ice")

#get RC explanation. Counts occurence.
import collections

def thestring(s):

    d = collections.defaultdict(int)
    for c in s:
        d[c] += 1
    for c in sorted(d, key=d.get, reverse=True):
        print '%s %6d' % (c, d[c])


thestring("pizza")
thestring('icecream')

# Write a method that takes in two numbers. Return the greatest
# integer that evenly divides both numbers. You may wish to use the
# `%` modulo operation.

def twonum(a,b):
    #ask why this does not work
    # for loop for numbers upto given
    #this is recursion
    #for i in range(1,j):
        #if i > 1:
            #if i % j == 0 and i % q == 0:
                #print i
    if b == 0:
        return a
    else:
        return twonum(b, a % b)

print twonum(10,20)
print twonum(3,12)
print twonum(10,55)

#also built in
from fractions import gcd
gcd(20,8)
#should produce >>> 4


#interesting algo from interactive python
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

moveTower(3,"A","B","C")
