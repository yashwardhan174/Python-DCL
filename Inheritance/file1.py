#Single Level Inheritance

class Student(): #parent class
    def study(self): #IM in parent class
        print("Every Student should study")

class EngineeringStudent(Student): #child class
    def present_project(self): #IM in Child class
        print("Engineering students are expected to do project")

es = EngineeringStudent() #instantiation
es.present_project() #using childobjref , access child IM
es.study() #accessing parent class Instance method using childobjreference
print(EngineeringStudent.__mro__)

print("----------------------")

class Developer:
    def build(self):
        print("Developers build applications")

class FrontendDeveloper(Developer):
    def design_website(self):
        print("Frontend Developer Desing UI and Frontend of a Webpage")


d1 = FrontendDeveloper()
d1.design_website()
d1.build()