import time
print("\033[1;033m")
for i in range(1,11):
    time.sleep(2)
    for j in range(1,11):
        print("{:02d}".format(i*j),end=" ")
    print()
    
