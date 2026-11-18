#Variable Keyword ASrguments

def gather(**kwargs): #packing
    print(kwargs)

gather(name="Yash" , age=10 ,marks=50)

def disperse(name,age,marks):
    print(name)
    print(age)
    print(marks)

d = {"name":"Yash" , "age" : 10 ,"marks":50}
disperse(**d) #unpacking


def together(**kwargs):
    print(kwargs)

d = {"name":"Yash" , "age" : 10 ,"marks":50}

together(**d)