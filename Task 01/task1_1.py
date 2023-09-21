temp1 = input()
temp=[]
temp=temp1.split(" ")
n=int(temp[0])
x=int(temp[1])
temp=[]
allmarks=[]
y=[]
for i in range(x):
    temp1=input()
    temp=temp1.split(" ")
    allmarks.append(temp)
    temp=[]
    y+=allmarks[i]
marks_db=zip(*allmarks)

marks_sum=0
for i in marks_db:
    for j in i:
        marks_sum+=float(j)
    print(marks_sum/x)
    marks_sum=0