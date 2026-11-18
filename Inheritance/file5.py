#Hubrid Inheiotance

class Player:
    def play(self):
        print("A player is a athelete")

class Batsman(Player):
    def bat(self):
        print("A batsman scores runs")

class Bowler(Player):
    def bowl(self):
        print("A bolwer takes wickets")

class Allrounder(Batsman , Bowler):
    def field(self):
        print("Allrounder does everything")

p1= Allrounder()
p1.field()
p1.bat()
p1.bowl()
p1.play()


class Employee:
    def emp(self):
        print("Employee works in a company")

class FrontendDev(Employee):
    def ui(self):
        print("Front end Developer Builds a UI")

class BackendDev(Employee):
    def logic(self):
        print("Backend Developer Builds a Logic ")

class FullStackDev(FrontendDev , BackendDev):
    def Saas(self):
        print("Full_Stack Developer Does Both Frontend And Backend")

fsd = FullStackDev()
print(FullStackDev.__mro__)
fsd.Saas()
fsd.emp()
fsd.logic()
fsd.ui()