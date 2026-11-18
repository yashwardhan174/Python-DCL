#Hierarchial Inheritance

class Minsiter:
    def attend_meeting(self):
        print("Misiter Will attend Meeting")

class EducationMinsiter(Minsiter):
    def education_reform(self):
        print("Education Policies")

class FinanceMinister(Minsiter):
    def budget_speech(self):
        print("Country Budget ")

class HealthMinsiter(Minsiter):
    def inspect_govt_fac(self):
        print("Define Basic Helath Needs")


m1 = HealthMinsiter()
m1.inspect_govt_fac()
m1.attend_meeting()

print("------------")

m2 = FinanceMinister()
m2.budget_speech()
m2.attend_meeting()

print("--------------")

m3 = EducationMinsiter()
m3.education_reform()
m3.attend_meeting()

print("--------------")