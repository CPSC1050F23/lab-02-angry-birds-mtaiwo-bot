"""
Author:         YOUR NAME
Date:           DATE
Assignment:     Lab 01
Course:         CPSC1051
Lab Section:    SECTION

CODE DESCRIPTION

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
launch_angle = float(input())
# Convert launch angle from degrees to radians
launch_angle_radians = math.radians(launch_angle)

print("What is the height of the slingshot in feet?")
# Get the height of the slingshot as input
slingshot_height = float(input())

# Calculate the duration of the flight in seconds
total_flight_time = 2 * intial_velocity * math.sin(launch_angle_radians)/ GRAVITY

# Calculate the maximum horizontal distance
horizontal_distance = intial_velocity * math.cos(launch_angle_radians) * total_flight_time

# Calculate the maximum height
max_height = slingshot_height + (intial_velocity * math.sin(launch_angle_radians))**2/ 2*GRAVITY

# Print out the calculated metrics like below. Replace X with the calculated numbers. Shorten the numbers to 2 significant figures (0.02, 12.44, etc.)
    # Duration of flight:  seconds
    print(f"{total_flight_time:.2f}") 
    # Bird's maximum horizontal distance:  feet
    print(f"{horizontal_distance:.2f}")
    # Bird's maximum height:  feet
    print(f"{max_height:.2f}")

    # The duration of the bird's flight in seconds
    print(total_flight_time)
    # The bird's maximum possible horizontal distance
    print(horizontal_distance)


# STEP 2

print("Enter the x-coordinate of the pig:")
# Get the pig's x-coordinate as input


print("Enter the y-coordinate of the pig:")
# Get the pig's y-coordinate as input


# Calculate the straight-line distance from the bird & slingshot to the pig


# Print it out as below. Replace X with the calculated numbers. Shorten the numbers to 2 significant figures (0.02, 12.44, etc.)
    # Straight-line distance to the pig: X feet


# Calculate the time when the bird is directly over the pig (x1, y1)


# Calculate the y-position of the bird at the time it is directly over pig



# Print it out as below. Replace X with the calculated numbers. Shorten the numbers to 2 significant figures (0.02, 12.44, etc.)
    # The bird will be over the pig at time X seconds. The bird will be X feet above the pig.



# STEP 3

print("Enter the time in seconds to calculate the bird's position:")
# Get the time as input


# Calculate the x and y coordinates of the bird at the inputted time


# Print the results like below. Replace X & Y with calculated numbers. Shorten the numbers to 2 significant figures (0.02, 12.44, etc.)
    # Coordinates of bird at X seconds: X, Y
