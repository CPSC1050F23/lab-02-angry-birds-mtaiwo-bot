"""
Author:         Folu Taiwo
Date:           9/5/23
Assignment:     Lab 01
Course:         CPSC1051
Lab Section:    003

CODE DESCRIPTION: The objective is to get the bird to hit the pig by 
finding the coordinates of the bird and the time when it hits the pig.
"""


import math

GRAVITY = 32.1522

print("Welcome to the Angry Birds aimbot! Go pig or go home!")

# STEP 1

print("What is the bird's initial velocity?")
# Get the bird's initial velocity as input
intial_velocity = float(input())

print("What is the bird's launch angle in degrees?")
# Get the bird's launch angle as input
theta = float(input())
# Convert launch angle from degrees to radians
theta_radians = math.radians(theta)

print("What is the height of the slingshot in feet?")
# Get the height of the slingshot as input
slingshot_height = float(input())

# Calculate the duration of the flight in seconds
time = (2 * intial_velocity * math.sin(theta_radians))/GRAVITY

# Calculate the maximum horizontal distance
horizontal_distance = intial_velocity * math.cos(theta_radians) * time

# Calculate the maximum height
height = (slingshot_height) + ((intial_velocity*math.sin(theta_radians))**2)/(2*GRAVITY)

# Print out the calculated metrics like below. Replace X with the calculated numbers. Shorten the numbers to 2 significant figures (0.02, 12.44, etc.)
    # Duration of flight: seconds
print(f"Duration of flight: {time:.2f} seconds") 
    # Bird's maximum horizontal distance: feet
print(f"Bird's maximum horizontal distance: {horizontal_distance:.2f} feet")
    # Bird's maximum height: feet
print(f"Max height of the bird: {height:.2f} feet")
   
    # The duration of the bird's flight in seconds

    # The bird's maximum possible horizontal distance



# STEP 2

print("Enter the x-coordinate of the pig:")
# Get the pig's x-coordinate as input
x1 = float(input())
x2 = 0

print("Enter the y-coordinate of the pig:")
# Get the pig's y-coordinate as input
y1 = float(input()) 
y2 = slingshot_height

# Calculate the straight-line distance from the bird & slingshot to the pig
straight_line_distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
#x1,y1 are the pigs coordinates.
#x2,y2 are the birds from the slingshot so 0 and the height of the slingshot.

# Print it out as below. Replace X with the calculated numbers. Shorten the numbers to 2 significant figures (0.02, 12.44, etc.)
    # Straight-line distance to the pig: X feet
print(f"Straight-line distance to the pig: {straight_line_distance:.2f} feet")

# Calculate the time when the bird is directly over the pig (x1, y1)
pig_time = x1/(intial_velocity*(math.cos(theta_radians)))

# Calculate the y-position of the bird at the time it is directly over pig
vertical_height = slingshot_height + intial_velocity*(math.sin(theta_radians))*pig_time - 0.5*(GRAVITY)*(pig_time**2)

# Difference between the birds height and the pig's height:
vertical_distance = vertical_height - y1

# Print it out as below. Replace X with the calculated numbers. Shorten the numbers to 2 significant figures (0.02, 12.44, etc.)
    # The bird will be over the pig at time X seconds. The bird will be X feet above the pig.
print(f"The bird will be over the pig at time {pig_time:.2f} seconds. The bird will be {vertical_distance:.2f} feet above the pig.")


# STEP 3

print("Enter the time in seconds to calculate the bird's position:")
# Get the time as input
time = float(input())

# Calculate the x and y coordinates of the bird at the inputted time
horizontal_position = intial_velocity*math.cos(theta_radians)*time
vertical_position = slingshot_height + intial_velocity*(math.sin(theta_radians))*time - 0.5*GRAVITY*(time**2)
# Print the results like below. Replace X & Y with calculated numbers. Shorten the numbers to 2 significant figures (0.02, 12.44, etc.)
    # Coordinates of bird at X seconds: X, Y
print(f'Coordinates of bird at {time} seconds: ({horizontal_position:.2f}, {vertical_position:.2f})')