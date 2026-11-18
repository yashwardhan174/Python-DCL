# r mode / read mode

# f = open("filehandling/demo2.txt","r") if file is not present then filenotfound error will be thrown

f = open("filehandling/demo1.txt","r")

print(f.name) #file which is open
print(f.mode) #mode in which open
print(f.closed) #checks file is closed or not

print(f.readable()) #checks if file is readable or not
print(f.writable()) #chewcks if file is writable or not

#specific read methods

print(f.read()) #reads the data from opened file

print(f.read(10)) #reads the data upto n charecters (spaces are charecters)

print(f.readline()) #reads till end of a line in form a string
print(f.readline(5)) #reads till n charecter of a line

print(f.readlines()) #it returns lines as list of string : each string is a line

# f.write("hii") : if we perform write op. in read mode , it will throw Unsupportedoperation error

f.close() #it will close the file 
print(f.closed)

