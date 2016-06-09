"""
Luc Pitre
25 May 2016
Text based game, exercise 1
"""

#here i create a character, i give the character a name
johnny = {'name':'Johnny'}
sally= {'name': 'sally', 'age': 10,'speed' :100} 
#above is called a dictionary, more on this later
"""
johnny, on the left side of the equal sign, is the name of the group of data,
which is inside of the curly braces on the right side of the equal sign
So, name of the data is on the left, the data itself is on the right
"""
#here johnny will get his health set, the health attribute is being added
johnny['health'] = 100;

#here johnny's info is printed out on the screen
print("Hi! I'm " + johnny['name'] + "! I have " + str(johnny['health']) + " health.");

#add one attribute to johnny right below this, maybe hair color, hne 16
johnny['speed'] =30;
#now print out johnny's new attribute
#if you need help look at line 19
print("Hi! I'm " + johnny['name'] + "! I have " + str(johnny['speed']) + " speed.");
print("Hi! I'm " +sally['name'] + "! I have " + str(sally['age']) + " age")
def rase():
    print("jony and sally have a rase")
    if johnny ["speed"]>sally ["speed"]:
        print('johnny wins')
    if johnny ["speed"]<sally ["speed"]:
        print('sall wins')
rase()
