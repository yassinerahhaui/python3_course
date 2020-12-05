# dictionary

mydict = {"key1":"value1","key2":"value2","key3":"value3"}

print(mydict,type(mydict))

print(mydict["key1"])


for item in mydict:
    print(item, mydict[item])

mydict["key1"] = "value1Update"

print("---------")
print(mydict["key1"])