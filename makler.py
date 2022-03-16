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
# Make sure to run this in Python 3.

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
        tmpInput = input(prompt + " [y/n]\n")
        if(tmpInput in {"y", "n"}):
            return True if tmpInput == "y" else False 
            # The return statement immediately breaks out of the entire function
        else:
            print("Invalid input. Please try again.")

def inputMeters(prompt): # Take an input, then check if it's a number
    while(True):
        try: # Try something that might make the program crash
            tmpInput = int(input(prompt + "(in m)\n"))
        except ValueError: # If we'd crash because the input is not a number, do this instead
            print("Invalid input. Please try again.")
        else:
            return tmpInput

# Initialize global variables that we'll need throughout the program, among them a rooms list.
rooms = []
continueInput = True
totalArea = 0

# Define strings that will be used multiple times - this saves code
firstSidePrompt = "What is the length of the first side touching it?"
otherSidePrompt = "What is the length of the other side touching it?"

# Make the user comfortable
print("--------------------------------\n")
print("Hello Mister Makler!\n")

# Let the user input the measurements of a room, repeating until they choose to stop.
# Each iteration gathers the measurements of 1 room and then adds it to the rooms list.
while (continueInput):
    print("--------------------------------\n")
    if(len(rooms) == 0): print("Please proceed with your first room.")
    tmpIsRectangle = inputYN("Is the room a rectangle?")

    if(tmpIsRectangle):
        print("\nMove to any corner of the room.")
        tmpOuterX = inputMeters(firstSidePrompt)
        tmpOuterY = inputMeters(f"\n{otherSidePrompt}")
        tmpInnerX = None
        tmpInnerY = None
    else:
        print("\nMove to the corner with the inward angle.")
        tmpInnerX = inputMeters(firstSidePrompt)
        tmpInnerY = inputMeters(f"\n{otherSidePrompt}")
        print("\nNow move to the corner opposite of the inward angle.")
        tmpOuterX = inputMeters(firstSidePrompt)
        tmpOuterY = inputMeters(f"\n{otherSidePrompt}")
    
    rooms.append(Room(tmpIsRectangle, tmpOuterX, tmpOuterY, tmpInnerX, tmpInnerY))
    print("--------------------------------\n")
    roomWord = "room" if len(rooms) == 1 else "rooms" # Apparently this can't be placed inside an f-string without looking weird
    print(f"\nYou have added {len(rooms)} {roomWord} so far.")
    continueInput = inputYN("Would you like to enter an additional room?")

for room in rooms: 
    totalArea += room.calculateArea()

print("--------------------------------\n")
print(f"The total area to all rooms combined\nequals {totalArea} m².")