# a mode / append mode
f = open("filehandling/demo3.txt","a") #if file is not present it creates a new file and adds the data
# f = open("filehandling/demo2.txt","a") #it does not remove existing data , just add new data in it.

f.write("This is append mode")

f.close()