# r+ mode 

# f = open("filehandling/demo4.txt","r+") if file is not present , it will throw an error
f = open("filehandling/demo3.txt","r+")

print(f.read())

f.write("I am Yash")

f.close()