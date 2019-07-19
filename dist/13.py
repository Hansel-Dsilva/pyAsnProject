count = 0
str1 = input("String : ")
substr = input("Substring : ")
for i in range(len(str1)):
    if str1[i : i+len(substr)] == substr:
        count += 1
print("\n" + substr + " occurs " + str(count) + ' times.')