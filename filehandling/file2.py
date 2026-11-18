# w mode / write mode

f = open("filehandling/demo2.txt","w") #if this file is not preswent , it will create a file of this name 
# f = open("filehandling/demo1.txt","w") #if we open file in w mode , earlier content is erased only your content will be visible
# f.write("I am learning file handling")

f.writelines(["a for apple\n","b for balls\n", "c for cat\n"])
f.close()