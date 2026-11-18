con_name = "Spain"
result = "won"
sport = "Football"
opp = "Argentina"

new_str = con_name+" "+result+" " +"the"+" " + sport+" " +" Game against"+" "+ opp

print(new_str)

#Disadvantage
#1) Too many + operator
#2) Too many Explicit Typecasting


# player_name = input("Enter the Player Name")
# goals = int(input("Enter the Number Of goals Scored"))
# height = float(input("Enter the height Of player"))
# country = eval(input("Is he from Argentina"))

# # string = str(player_name) + " " + " is " + str(country) + " Argentine player who has scored" + " " + str(goals) +" goals and height is " + str(height)

# string = f"{player_name} is a {country} Argentinian player who has scored {goals} goals and height is {height}"

# print(string)
 

#to avoid these issue , new concept was introduced 
#String Formating - It is the process of inserting variables or values into a string template in a more readable manner without using + operator


#1) f-strings
name = "Cheetah"
speed = 78
weight = 24.5

new_string = f"{name} weighs {weight} kg and runs at {speed} kmph"
print(new_string)

#2) format method

n_s = "{} weighs{}kg and runs at {}kmph".format(name , weight , speed)
print(n_s)

