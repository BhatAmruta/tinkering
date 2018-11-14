#Control Structures
#while loop
import math
counter = 1
while counter <= 5:
    print("Hello, world")
    counter = counter + 1

# for loop
for item in [1,2,3,4,5]:
    print(item)

wordlist = ['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)
print(letterlist)

#if statement
n= int( input("enter value of n"))

if n < 0:
   print("Sorry, value is negative")
else:
   print(math.sqrt(n))

#nested if
score= int(input("enter you score in english"))
if score >= 90:
   print('A')
else:
   if score >=80:
      print('B')
   else:
      if score >= 70:
         print('C')
      else:
         if score >= 60:
            print('D')
         else:
            print('F')
#list comprehension
sqlist=[x*x for x in range(1,11)]
print(sqlist)
sqlist1=[x*x for x in range(1,11) if x%2 != 0]
print(sqlist1)
print([ch.upper() for ch in 'comprehension' if ch not in 'aeiou'])