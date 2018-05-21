mylist1 = [1, 2, 4, 5, 10, 20, 25, 50, 100]
mylist2 = [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 200]
commonfactor=[]
for num1 in mylist1:
    for num2 in mylist2:
        if num1 == num2:
            commonfactor.append(num1)
# Greatest common factor is the last entry of the list commonfactor
print(commonfactor[-1])

