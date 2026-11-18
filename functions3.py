#with parameteres & without return

def register(name , phn_no):
    # print(name ," registered successfully",phn_no)
    print(f"{name} registered successfully contact here->{phn_no}")

# u_name = "Yash"
# u_no = 9630421406
# register(u_name , u_no)

register("Yash",9630421406)
register("Akshat",1213546540)
register("Chindi",1541564)

def sendOTP(phn_no):
    print(f"OTP sent successfully to {phn_no}")

sendOTP(9630421406)