#one collection having another collection inside it
'''
1> nested list
2> nested dictionary
3> list of dictionary
3> dictionary of list
'''

l=[["Amy",80000,"BE"],["Ben",45000,"SSLC"],["Chad",89000,"Diploma"]]

# for i in l:
#     if i[1] > 50000:
#         print(i[0])

l[1].append("M.Tech")
print(l[1])