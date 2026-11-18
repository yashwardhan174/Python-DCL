#Universal : try-except-else-finally

print("start")
try:
    print(7/0)
except Exception:
    print("Exception handled")
else:
    print("Else Block executed when no error occurs")
finally:
    print("Finally executes always wrt try block")

print("end")
