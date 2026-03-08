

set1={"a","b","c"}
dict1=dict()
count=10
for key in set1:
    dict1[key]=count
    count=count+10
print(dict1)

# set1={"a","b","c"}
# dict1=dict()
# for key in set1:
#     dict1[key]=None
# print(dict1)

# set1={"a","b","c"}
# dict1={key:None for key in set1}
# print(dict1)