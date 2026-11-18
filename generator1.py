#creating generator function
#LAZY evaluator
def fun(): #gemnerator func is created 
    print("hii")
    # yield 10 #yield keyword is mandatory for creating yield keyword
    # yield 20
    # yield 30
    # yield 40

    #creating custom Sequence
    # value = 1
    # yield value**1 
    # value+=2
    # yield value**2
    # value+=3
    # yield value**3
    # value+=4
    # yield value**4
    value = "A"
    yield value*1
    value = "B"
    yield value*2
    value = "C"
    yield value*3
    value = "D"
    yield value*4
gen_obj = fun() #generator object is created when generator obeject is called
print(gen_obj)

#1st approach using next()
# print(next(gen_obj)) #it will returns the yielded value and now func is paused
# #to resume generator func call func obj again

# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))

#2nd approach using for loop

# for i in gen_obj:
#     print(i)

#3rd approach is by explicit type casting

print(list(gen_obj))