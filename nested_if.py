'''
we can place one if condition inside another if condition , to check multiple levels of conditions

Note : When we need to check a condition which is present inside anopther conditon
- 
'''
mail = "yash@gmail.com"
pwd = "123"

user_mail = input("Enter yopur mail")

if mail == user_mail:
    user_pwd = input("Enter your pass")
    if pwd == user_pwd:
        print("Login Successful")
    else :
        print("Invalid Password")
else:
    print("Wrong mail entered")
