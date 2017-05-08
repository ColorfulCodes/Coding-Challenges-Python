# Write a method that takes in a string and returns the number of
# letters that appear more than once in the string. You may assume
# the string contains only lowercase letters. Count the number of
# letters that repeat, not the number of times they repeat in the
# string.


"""

def sduplicate(s):
    emp =[]
    count = 0
    for i in s:
        if i not in emp:
            emp.append(i)
        elif i in s:
            count += 1

    return emp

print sduplicate("assume")
print sduplicate("team")
print sduplicate("mississippi")
"""
