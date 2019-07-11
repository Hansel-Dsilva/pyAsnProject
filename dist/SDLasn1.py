
f = open('q.txt', 'r')
print("Press Q to display question list")

while 1:
    Qno = input("Enter question no. : ")
    if Qno == 'Q' or Qno == 'q':
        print(f.read())
    elif int(Qno) in range(1, 66):
        exec(open(Qno + ".py").read())
    else:
        print("INVALID INPUT! PLEASE REFER THE QUESTION LIST BY ENTERING 'Q'")
        continue