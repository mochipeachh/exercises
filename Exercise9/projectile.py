from math import pi, tan, cos

# Barrel height is in metres
initialBarrelHeight = float(input("what is your initial height"))

# Distance is in metres
horizontalDistance = float(input("what is your distance"))

# Gravity is metres per second squared
gravity = 9.81

# Velocity is metres per second
velocity = float(input("what is your velocity"))

# Angle is in degrees
angleInDegrees = float(input("what is your angle"))

# Angle conversion from degrees to radians
angleInRadians = angleInDegrees * (pi/180)


def calculate_maximum_height(start_height, distance, grav, initial_velocity, angle):
    result = start_height + distance * tan(angle) - (grav * distance ** 2) / (
                2 * (initial_velocity * cos(angle)) ** 2)

    print(result)


calculate_maximum_height(initialBarrelHeight, horizontalDistance, gravity, velocity, angleInRadians)
