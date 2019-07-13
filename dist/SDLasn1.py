print("Press 0 to display question list")

ls1 = []
for i in range(66):
    ls1.append(str(i))
while 1:
    Qno = input("Enter question no. : ")
    if Qno not in ls1:
        print("INVALID INPUT! PLEASE REFER THE QUESTION LIST BY ENTERING '0'")
        continue
    elif not int(Qno):
        f = open('q.txt', 'r')
        print(f.read())
        f.close()
    else:
        try:
            exec(open(Qno + ".py").read())
        except FileNotFoundError:
            print("Oops! Looks like " + Qno + " hasn't been solved yet.\nContribute by uploading " + Qno + ".py to https://github.com/Hansel-Dsilva/pyAsnProject/dist")