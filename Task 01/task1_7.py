l1=65
n1=1
for i in range(5):
    for j in range(i+1):
        if i%2==0:
            print(chr(l1),end=" ")
            
        else:
            print(n1,end=" ")
        l1+=1
        n1+=1
    print()
