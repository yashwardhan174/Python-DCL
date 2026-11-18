#It is used in API or Data frame in Pandas

company = {
    'names' : ['Amy' , 'Ben' , 'Chad'],
    'age' : [21 , 32 , 45],
    'salaries' : [82000 , 48000 , 36000],
    'depts' : ['HR' , 'Sales' , 'Accounts']
} 

for i in company['names']:
    print(i)
print("----------")
for i in company.values():
    print(i[0])