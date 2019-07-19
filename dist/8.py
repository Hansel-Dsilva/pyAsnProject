str1 = input("Sample String : ")
dict1 = {}
for i in str1:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1
print(dict1)