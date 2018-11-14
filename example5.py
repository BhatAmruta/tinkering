#input prompt
aName = input("Please enter your name ")
print("Your name in all capitals is",aName.upper(),
      "and has length", len(aName))
#input data for circle
sradius = input("Please enter the radius of the circle ")
radius = float(sradius)
diameter = 2 * radius
print(radius)
print(diameter)
print("Hello","World", sep="***")
print("Hello","World", end="***")
#string formatting
price = 24
item = "banana"
print("The %s costs %d cents"%(item,price))
print("The %+10s costs %10.2f cents"%(item,price))
itemdict = {"item":"banana","cost":24}
print("The %(item)s costs %(cost)7.1f cents"%itemdict)