#It is used when there are multiple considtions to check and ONLY 1st Matching condition and its block will be executed

#Note : When we want many choices but only one should apply
#elif is a keyword in  python and can be repeated any number of times
#else must come at the last and only once (else is optional)
num = int(input("Enter your marks"))

if num>90 and marks<=100:
    print("Topper")
elif num>80 and num<=90:
    print("Distinction")
elif num>60 and num<=80:
    print("1st Class")
elif num>40 and num<=60:
    print("2nd class")
elif num>35 and num<=40:
    print("Pass")
elif num<35 and num>=0:
    print("Fail")
else:
    print("Invalid Input")