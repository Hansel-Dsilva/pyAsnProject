str1 = input("String : ")
n = 1
while n < len(str1):
    print(n)
    str1 = str1.replace(str1[n], '')
    n += 1
print("String now : " + str1)
