number=["Niha","Neha","Nithu","Pavani","Manu"]
marks= [45,50,67,28,33]
p=1
for i in range(5):
    if marks [i]>40:
        print("{}. {} has scored {}%".format (p,number[i],marks[i]))
        p=p+1
