names=["Niha","Harika","Ammu","kalyani","nithin"]
marks=[[20,30,40],[44,55,66],[77,88,99],[45,55,67],[89,99,67,]]
for i in range(5):
    a=sum(marks[i])//3
    print("{} . {} has scored {}".format(i+1,names[i],[a]))
