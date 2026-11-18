#approach 3:

print("Start")
print(1)

l = [10,20,30,40]

try:
    p = int(input("Enter 1st Number"))
    q = int(input("Enter 2nd Number"))

    print(p/q)
    print(l[q])

except ValueError as e1:
    print(e1)

except ZeroDivisionError as e2:
    print(e2)

except IndexError as e3:
    print(e3)

print("End")