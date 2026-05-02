number=list(map(int, input ("Enter numbers separeted by space: ").split()))

largest=second=99999

for num in numbers:
    if num > largest:
        second=largest
        largest=num
    elif num > second and num !=largest:
        second=num
print("second largest number:",second)        
