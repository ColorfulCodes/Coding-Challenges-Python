def unique(x):
    if len(x) == 1:
        return True
    else:
        emp = []
        for i in x:
            if i not in emp:
                emp.append(i)
            else:
                return False
        return True

print unique("string")
print unique("pizza")
print unique("I")
print unique("Delivery")
print unique("style")
