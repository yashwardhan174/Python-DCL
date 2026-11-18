#nested try-except

print("start")
try:
    print("outer try block")

    try:
        print("inner try block")

    except Exception:
        print("inner except block")

except Exception:
    print("Outer Exept Block")

else:
    print("Else Block")
    
finally:
    print("Finally Block")

print("end")