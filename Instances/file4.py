class Trainer :
    pass

t1 = Trainer()
t1.name = "Chetan BK"
t1.subject = "Python"
t1.id = 101

t2 = Trainer()
t2.name = "Sanjay Raghuwanshi"
t2.subject = "SQL"
t2.id = 102

t3 = Trainer()
t3.name = "Ravi Shastry"
t3.subject = "Frontend"
t3.id = 103

print(t1.__dict__)
print(t2.__dict__)
print(t3.__dict__)