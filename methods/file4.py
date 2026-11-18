class Student:
    def __init__(self , name ,roll):
        self.name = name #IV1
        self.roll = roll #IV2

    @staticmethod #not dependent on self or cls 
    def calc_percentage(marks , total_marks): #static method /utility method : (it is related to Strudent class , thats why it is created)
        print((marks/total_marks)*100)

Student.calc_percentage(483 , 900)



