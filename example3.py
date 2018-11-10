#string
myName = "David"
print(myName)
print(myName[3])
#repeat string
print(myName*2)
#string length
print( len(myName))
print( myName.upper())
print(myName.center(10))
print(myName.find('v'))
print(myName.split('v'))
#string method
mySet={False, 4.5, 3, 6, 'cat'}
yourSet = {99,3,100}
print(mySet.union(yourSet))
print(mySet | yourSet)
print(mySet.intersection(yourSet))
print(mySet & yourSet)
print(mySet.difference(yourSet))
print( mySet - yourSet)
print({3,100}.issubset(yourSet))
print({3,100}<=yourSet)
print(mySet.add("house"))
print(mySet.remove(4.5))
print(mySet.clear())