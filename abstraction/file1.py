from abc import ABC , abstractmethod

class Application(ABC):
    @abstractmethod
    def login(self):
        pass

class WebApplication(Application):
    def login(self):
        print("Enter Username and Password")

wa = WebApplication()
wa.login()