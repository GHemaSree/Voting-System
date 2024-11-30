vote=[]
data=[]
result=[0,0,0,0,0]
option=["BJP","Congress","BRS","TDP","Nota"]
draw=[]
cnt=0
while(1):
    user=[]
    age=int(input("Enter your age: "))
    if(age>=18):
        print("WELCOME TO ABC CONSTITUENCY")
        name=input("Enter your name: ")
        id=int(input("Enter your id: "))
        if id>=2000 and id<=8999:
            if id not in vote:
                print("======================")
                print("Option 1: BJP")
                print("Option 2: Congress")
                print("Option 3: BRS")
                print("Option 4: TDP")
                print("Option 5: Nota")
                print("======================")
                a=int(input("Cast your vote:"))
                if 1<=a<=5:
                    result[a-1]+=1
                    vote.append(id)
                    user.append(name)
                    user.append(age)
                    user.append(id)
                    vote.append(user)
                else:
                    print("INVALID OPTION")
                    continue
            else:
                print("VOTING ALREADY COMPLETED")
                continue
        else:
            print("NOT IN RANGE")
            continue
    else:
        print("NOT ELIGIBLE TO VOTE")
        continue
    print("%s vote casted successfully thank you!!"%(id))
    cnt+=1
    if (cnt==2):
        print("Voting process completed")
        break
    continue
for i in range(len(result)):
    print("%s:%d"%(option[i],result[i]))
win=max(result)
i=result.index(win)
print("Winner is %s with votes %d"%(option[i],win))




