# Accepts any number of room measurements, then calculates the total area. 
# It is assumed that
# * rooms only consist of right angles.
# * rooms only have 1 inward angle at most.
# 
# Basically, this program assumes rooms either look like this:
#
#  ________________
# |                |
# |                |
# |                |
# |________________|
#
# or like this:
#
#  _______
# |       |
# |       |________
# |                |
# |                |
# |________________|
# 
# Make sure to run this in Python 3. Python 2 doesn't like my inputString function.

# Define what a room is (a bunch of lengths) and what it can do (calculate its area).
class Room:
    
    def __init__(self, isRectangle, outerX, outerY, innerX, innerY):
        self.isRectangle = isRectangle
        self.outerX = outerX
        self.outerY = outerY
        self.innerX = innerX
        self.innerY = innerY

    def calculateArea(self):
        if(self.isRectangle):
            return self.outerX * self.outerY
        else:
            return (self.outerX * self.outerY) - (self.innerX * self.innerY)

# Define functions that we'll to call more than once later.
# This should make the code below more readable.
def inputYN(prompt): # Take an input, then check if it's "y" or "n"
    while(True):
        tmpInput = input(prompt + "\n")
        if(tmpInput in {"y", "n"}):
            return True if tmpInput == "y" else False 
            # The return statement immediately breaks out of the loop and the function
        else:
            print("Invalid input. Please try again.\n")

def inputInt(prompt): # Take an input, then check if it's a number
    while(True):
        try: # Try something that might make the program crash
            tmpInput = int(input(prompt + "\n"))
        except ValueError: # If we'd crash because the input is not a number, do this instead
            print("Invalid input. Please try again.\n")
        else:
            return tmpInput

# Initialize global variables that we'll need throughout the program, among them a rooms list.
rooms = []
continueInput = True
totalArea = 0

# Make the user comfortable
print("--------------------------------")
print("")
print("Hello Mister Makler!")
print("")

# Let the user input the measurements of a room, repeating until they choose to stop.
# Each iteration gathers the measurements of 1 room and then adds it to the rooms list.
while (continueInput):
    print("--------------------------------")
    if(len(rooms) == 0): print("Please proceed with your first room.")
    tmpIsRectangle = True if inputYN("Is the room a rectangle? [y/n]") else False

    if(tmpIsRectangle):
        print("\nMove to any corner of the room.")
        tmpOuterX = inputInt("What is the length of the first side touching it? (in m)")
        tmpOuterY = inputInt("\nWhat is the length of the other side touching it? (in m)")
        tmpInnerX = None
        tmpInnerY = None
    else:
        print("\nMove to the corner with the inward angle.")
        tmpInnerX = inputInt("What is the length of the first side touching it? (in m)")
        tmpInnerY = inputInt("\nWhat is the length of the other side touching it? (in m)")
        print("\nNow move to the corner opposite of the inward angle.")
        tmpOuterX = inputInt("What is the length of the first side touching it? (in m)")
        tmpOuterY = inputInt("\nWhat is the length of the other side touching it? (in m)")
    
    rooms.append(Room(tmpIsRectangle, tmpOuterX, tmpOuterY, tmpInnerX, tmpInnerY))
    print("--------------------------------")
    if(len(rooms) == 1):
        print("\nYou have added 1 room so far.")
    else:
        print("\nYou have added " + str(len(rooms)) + " rooms so far.")
    continueInput = inputYN("Would you like to enter an additional room? [y/n]")

for room in rooms: 
    totalArea += room.calculateArea()

print("--------------------------------")
print("The total area to all rooms combined\nequals " + str(totalArea) + "m.")