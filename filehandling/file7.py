#x : exclusive

# f = open("filehandling/demo4.txt",'x') file exists error
f = open("filehandling/demo5.txt",'x') #new file not present
f.write("hi this is x mode")