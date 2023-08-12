import pandas as pd
df = pd.read_csv('stu.csv')
print(df)
print("-"*50)

glist=list(df.GPA)
print("\n the list of gpa: ",glist)

avg=sum(glist)/len(glist)
print(avg)

#df.insert(2, , 4)

x=input("Enter id")
y=input("Enter student name: ")
z=float(input("Enter student gpa: "))

glist.insert(2,z)
print(glist)