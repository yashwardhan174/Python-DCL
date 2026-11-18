class MovieTicket:
    theater = "INOX"
    gst = 18

    def __init__(self , seatno , moviename  , is_adult):
        self.seatno = seatno
        self.moviename = moviename
        self.is_adult = is_adult

    @classmethod
    def display_details(cls):
        print(cls.theater , cls.gst)

    def ticket_details(self):
        print(self.seatno , self.moviename , self.is_adult)

    @staticmethod
    def calculate_bill(ticket_price , quantity , gst):
        total = ticket_price*quantity
        gst_amount = total * gst/100
        return total + gst_amount

    def change_seat(self,new_seat):
        self.seatno = new_seat

t1 = MovieTicket(18 , "Toxic" , True)
t2 = MovieTicket(19 , "Toxic" , False)

t1.display_details()
t1.ticket_details()
t1.change_seat(35)

print("--------------")

t2.display_details()
t2.ticket_details()
t2.change_seat(36)

print("-----------------")

bill = MovieTicket.calculate_bill(500 , 2 , MovieTicket.gst)
print(bill)

print("-----------------")