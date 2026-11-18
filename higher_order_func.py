# def python_exam(): #Callback fucntion
def python_exam(location): 
    print("Python exam Conducted",location)

# def java_exam(): #callback fucntion
def java_exam(location): 
    print("Java Exam Conducted",location)

def start_exam(subject): #Higher Order Fucntion
    subject("Indore")

start_exam(python_exam)
start_exam(java_exam)