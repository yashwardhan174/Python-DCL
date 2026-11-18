s1 = "good evening students"

#1) ref.capitalize() : It returns a copy of a streing in capitalize format(1st Lettter of 1st word capital)

print(s1.capitalize()) #Good evening students
print(s1) #original is untouched

#2)ref.title() : It returns a copy of string in titlecased form(1st letter of Each word capital)

print(s1.title()) #Good Evening Students

#3)ref.upper() : It rerturns a copy of a string which is in UPPERCASE 

print(s1.upper()) #GOOD EVENINIG STUDENTS

#4) ref.lower() : It returns a copy of string in lowercase
s2 = "YASHWARDHAN"
print(s2.lower())

#5) ref.isupper() : It returns True , if the string is an UPPERCASE string else false
print(s2.isupper())
print("=========================")

#6) ref.islower() : It returns True , if the string is an lowercase string else false
print(s2.islower())

#7) ref.swapcase() : It returns a copy of a string with uppercase and lowercase letters swaped 
print("=========================")
s3 = "SPAIN are CHAmpions"
print(s3.swapcase())
print("=========================")
#8) ref.isalpha() : It returns True if string is an alphabetic string
s4 = "YOU cannot seeme"
print(s4.isalpha())
print("=========================")
#9) ref.isdigit() : It returns Ttrue if the string is containing only digits
s5 = "143"
print(s5.isdigit())
print("=========================")
#10) ref.isalnum() : It returns truue either string is having Alphabets or digits or both
s6 = "annabond2"
print(s6.isalnum())
print("=========================")
#11) ref.startswith("substring") : It returns true if the given string starts with the substring 
s7 = "big bang theory"
print(s7.startswith("b"))
print("=========================")
#12) ref.endswith("substring") : It returns True if the string endswith given substring
print(s7.endswith("theory"))

print("=========================")

#13) ref.replace("oldsubstring" , "newsubstring") : It returns a copy of a string whivh replaces the oldsubtring with newsubstring
s8= "hahahahahahah"

print(s8.replace("a" , "e"))
s9 = "robber was a robber living in a robber colony"
print(s9.replace("robber" , "police"))

print("=========================")

#14) ref.index("substring") : It returns the index number of the 1st occuring substring

s10 = "today is a cloudy day"
print(s10.index("a"))

#15) ref.count("substring") : It returns the number of time that substring is occuring

print(s10.count("a"))

#16) ref.lstrip() : it returns a copy of string which leading(left/beggining) whitespaces removed

s11  = "     ENOUGH!!!"
print(s11.lstrip())

#17) ref.rstrip() : right hand side ki spaces remove krdega
s12 = "OMG!!      "
print(s12.rstrip())

#18) ref.strip() : it returns a copy of string with leading and trailing(right/end) whitespaces removed

s13 = "    Yashwardhan Nigam       "
print(s13.strip())

#19) ref.split() : it returns list of substring/words split based on whitespaces

s14 = "Messi Is GOD of Football"
print(s14.split())
print(len(s14.split()))

s15 = "mia+khalifa+jonny+sins+lana+del+rey"
print(s15.split("+"))

s16 = "work.yashwardhan@gmail.com"

l = s16.split("@")
print(l[0])

#20) ref.join(collection of substrings) : It returns a copy of  a string with the refference joined btw substrings 

l2 = ["16" , "17" , "2026"]
print("-" .join(l2))
print("/" .join(l2))

