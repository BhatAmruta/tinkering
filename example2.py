#dynamic characteristics of variable
theSum = 0
theSum=theSum+1
theSum= True
print(theSum)
#heterogeneous list
myList = [1,3,True,6.5]
print(myList)
#repetition example
myList1 = [0] * 6
print(myList1)
myList2 = [1,2,3,4]
A = [myList2]*3
print(A)
myList2[2]=45
print(A)
#list methods example
myList3 = [1024, 3, True, 6.5]
myList3.append(False)
print(myList3)
myList3.insert(2,4.5)
print(myList3)
print(myList3.pop())
print(myList3)
print(myList3.pop(1))
print(myList3)
myList3.pop(2)
print(myList3)
myList3.sort()
print(myList3)
myList3.reverse()
print(myList3)
print(myList3.count(6.5))
print(myList3.index(4.5))
myList3.remove(6.5)
print(myList3)
del myList3[0]
print(myList3)
#range with list
range(10)
print(range)
print(list(range(10)))
print(list(range(5,10,2)))
print(list(range(10,1,-1)))