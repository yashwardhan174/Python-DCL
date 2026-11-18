#approach 4: Multiple Exceptions in one single except block

print("Start")
print(1)

l = [10,20,30,40]

try:
    p = int(input("Enter 1st Number"))
    q = int(input("Enter 2nd Number"))
    print(p/q)
    print(l[q])

except(ValueError , ZeroDivisionError,IndexError) as e:
    print(e)

print("end")