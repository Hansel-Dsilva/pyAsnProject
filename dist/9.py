str1 = input("Sample String : ")
for i in range(1, len(str1)):
    if str1[i] == str1[0]:
        str1 = str1[:i] + '$' + str1[i+1:]
print("Output : " + str1)
