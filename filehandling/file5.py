# w+ : write + read

f = open("filehandling/demo3.txt",'w+')
f.write("Good Evening")

print(f.tell()) #gives cursor position 
f.seek(0) #in the paranthesis give value where you want to put your cursor
print(f.tell())
print(f.read())

f.close()