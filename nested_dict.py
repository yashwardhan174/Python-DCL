company={
    "emp1" : {
        "name" : "Amy",
        "age" : 21,
        "salary" : 80000,
        "dept" : "Accounts"
    },
    "emp2" : {
        "name" : "Ben",
        "age" : 32,
        "salary" : 32000,
        "dept" : "Sales"
    },
    "emp3" : {
        "name" : "Chad",
        "age" : 44,
        "salary" : 49000,
        "dept" : "Marketing"
    }
}

# print(company.keys())

# for k in company.keys():
    # print(company[k])
    #or
    # print(company.get(k))
#OR
# print("-------------")
# for v in company.values():
    # print(v)

for k,v in company.items():
    print(v["name"])

#OR

for v in company.values():
    if v["salary"] > 48000:
        print(v["name"])

for v in company.values():
    if v["age"] > 40:
        v["salary"] = v["salary"]+5000
        print(v["salary"])
