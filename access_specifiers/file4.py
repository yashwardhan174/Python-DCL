class BusinessWoman:
    def __init__(self,name,category,profit):
        self.name = name
        self.category = category
        self.__profit = profit

    def __share_dividents(self):
        print("Dividents are distributed among angel investors")

    def file_ITR(self):
        print(self.__profit)
        self.__share_dividents()

b1 = BusinessWoman("Bani","Clothing",850000)
b1.file_ITR()