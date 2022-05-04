#Isiah Williams
#Coding For All-P6
#Mr. Burns

import algorithms

print("Menu of available functions: ") 
print("1 - Propeller Inner Angle")
print("2 - Viaduct Arches")
print("3 - Railway Slope")
print("4 - Suspension Bridge Arc Length")
  
choice = int(input("Please enter your menu choice: "))
quit = "Continue"

while quit == "Continue":
  
  if choice == 1:
    blades = int(input("How many blades are there?: "))
    print(f"The length of the angles are {algorithms.CalculateAngle(blades):.2f}")
  
  if choice == 2:
    length = float(input("What is the length of the viaduct: "))
    arches = int(input("How many arches are there?: "))
    print(f"The width of each arch is {algorithms.CalculateArchWidth(length, arches):.2f}")
    
  if choice == 3:
    x = float(input("What is the delta x value?: "))
    h = float(input("What is the delta h value?: "))
    print(f"The percent slope of the planned route is {algorithms.CalculatePercentSlope(x, h):.2f}%")
    
  if choice == 4:
    length = float(input("What is the length of the bridge?: "))
    height = float(input("What is the height of the bridge?: "))
    print(f"The arc length of the bridge is {algorithms.CalculateArcLength(length, height):.2f}")
    
  quit = input("Would you like to Quit or Continue?: ")
  
  if quit == "Continue":
    choice = int(input("Please enter your menu choice: "))
    