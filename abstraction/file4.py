from abc import ABC , abstractmethod

class Trainer(ABC):
    @abstractmethod
    def train(self):
        pass
    def conduct_mock(self):
        pass

class PythonTrainer(Trainer):
    def train(self):
        print("I will Train using Board and Laptop")

    def conduct_mock(self):
        print("Mock will condfucted Monthly")

class SqlTrainer(Trainer):
    def train(self):
        print("I will train using Videos demostration")

    def conduct_mock(self):
        print("Mock will be conducted at the end of course")

class FrontEndTrainer(Trainer):
    def train(self):
        print("I will Train using Notes and Laptop")

    def conduct_mock(self):
        print("Mock will conducted weekly")

p = PythonTrainer()
p.train()
p.conduct_mock()

s = SqlTrainer()
s.train()
s.conduct_mock()

f = FrontEndTrainer()
f.train()
f.conduct_mock()