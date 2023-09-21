n=[]
for i in range(6):
    if i==5:
        for k in range(11):
            if k%2!=0:
                print(" ",end="")
            else:
                print("*",end="")
        print()
    else: 
        for k in range(11):
            if (k!=5+i) and (k!=5-i):
                print(" ",end="")
            elif (k==5+i) or (k==5-i):
                print("*",end="")
        print()
    

    

