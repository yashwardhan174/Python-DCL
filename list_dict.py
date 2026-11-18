#List of Dictionary
'''
NOTE: JSON(javascript object notation) - It is a format to store and share structured data btw client and server in web apps , APIs

-> List of dict is used in JSON/API data
'''

company=[
    {
        "name" : "Amy",
        "age" : 21,
        "salary" : 80000,
        "dept" : "Accounts"
    },
    {
        "name" : "Ben",
        "age" : 32,
        "salary" : 32000,
        "dept" : "Sales"
    },
    {
        "name" : "Chad",
        "age" : 44,
        "salary" : 49000,
        "dept" : "Marketing"
    }
]

# print(company)
for i in range(2,-1,-1):
    # print(i)
    # print(i["name"])
    # if i['salary'] > 49000:
    #     print(i["name"])
    print(company[i]["name"])
