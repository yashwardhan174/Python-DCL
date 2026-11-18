#Multiple Inheritance

class Batsman:
    def bat(self):
        print("A batsman will score runs")

class Bowler:
    def bowl(self):
        print("A bowler will take wickets")

class Allrounder(Batsman , Bowler):
    def field(self):
        print("Allrounder does Batting and Bowling both")

a1 = Allrounder()
a1.field()
a1.bat()
a1.bowl()
print(Allrounder.__mro__)