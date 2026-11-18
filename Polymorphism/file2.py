from typing_extensions import override

class Minister:
    def address_public(self):
        print("Minister Will address to Public")

class Politician(Minister):
    @override
    def address_public(self):
        print("Politician WIll Make False Promises to Public")

p = Politician()
p.address_public()