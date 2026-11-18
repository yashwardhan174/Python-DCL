def counter():
    count = 0
    def increment():
        nonlocal count
        count = count+1
        print(count)
    return increment

inside = counter()
inside()
inside()
inside()

