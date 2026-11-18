# 'This module is explaining dunder variable '

# print(__package__) #gives package name
# print(__cached__) #gives file path of bytecode
# print(__doc__) #gives the doc string written at the very beggining of the file

def display():
    'this fucntion is used to display weekday'
    print("Today is Monday")

print(display.__doc__) #this is function docstring
