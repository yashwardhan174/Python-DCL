'''
#Working of Function :

-> When a function is created/defined, its implementation is stored in a method area/function area in memory, and a reference to this implementation is assigned to a variable named after the function. This variable is stored in a memory location called the stack area/main space.

-A function should have a body. If we need an empty function, we use the pass keyword inside the function body.

#How to Access/Call a Function:

- If we try to access a function without (), it will be treated as a normal variable that points to the function object.

-Therefore, to call/invoke/execute a function, use the function name followed by () with the appropriate arguments.

#Syntax:

function_name(arguments)

Example:

def greet(name):
    print("Hello", name)

greet("Yash")      # Function call
print(greet)       # Displays the function object (reference)


#Key Points:

-Function implementation is stored in the function/method area.
-The function name stores a reference to the function object.
-Every function must have a body.
-Use the pass keyword for an empty function.
-Writing only the function name (without ()) gives the function object/reference.
-Writing the function name followed by () executes the function.
'''