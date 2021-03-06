"""
Calculate the position of the planet at each timestep given an initial position
"""

total_time = 157_788_000
# total_time = 50_000
time_step = 25_000.0  # timestep
g = 6.67E-11  # gravitational constant
mass_sun = 1.9890e+30

# current position (x, y), velocity (x,y), and mass of each planet
earth = (1.4960e+11, 0.0000e0, 0.0000e0, 2.9800e+04, 5.9740e+24)
mars = (2.2790e+11, 0.0000e0, 0.0000e0, 2.4100e+04, 6.4190e+23)
mercury = (5.7900e+10, 0.0000e0, 0000.0e0, 4.7900e+04, 3.3020e+23)
venus = (1.0820e+11, 0.0000e0, 0.0000e0, 3.5000e+04, 4.8690e+24)

# compile into a single dictionary
planets = {"earth": earth, "mars": mars, "mercury": mercury, "venus": venus}

# grab each planet's tuple and it's key name
for name, planet in planets.items():
    # grab the values in each planet
    position_X = planet[0]
    position_Y = planet[1]
    mass_planet = planet[-1]
    velocity_X = planet[2]
    velocity_Y = planet[3]
    elapsed_time = 0

    while elapsed_time < total_time:
        # calculate the force between 2 bodies
        radial_distance = (position_X ** 2 + position_Y ** 2) ** (1/2)  # gives + & - roots
        force = g * (mass_planet * mass_sun) / -radial_distance ** 2  # use the - root

        # Force is a vector
        # calculate the X and y direction of force
        force_X = force * (position_X / radial_distance)
        force_Y = force * (position_Y / radial_distance)

        # Calculate the acceleration of a body
        # acceleration is the force proportional to the mass
        acceleration_X = force_X / mass_planet
        acceleration_Y = force_Y / mass_planet

        # approximate integration assuming acceleration constant within a time step
        velocity_X = velocity_X + acceleration_X * time_step
        velocity_Y = velocity_Y + acceleration_Y * time_step

        # calculate new position
        # this should be used in the next loop of while
        position_X = position_X + velocity_X * time_step
        # print(str(name) + " " + str(position_X) + " " + str(elapsed_time))
        position_Y = position_Y + velocity_Y * time_step

        # increase the elapsed time by the time step
        elapsed_time = elapsed_time + time_step
        # print(str(elapsed_time))

    # calculate new (last) position
    #position_X = position_X + velocity_X * elapsed_time
    # print(str(name) + " " + str(position_X) + " " + str(elapsed_time))
    #position_Y = position_Y + velocity_Y * elapsed_time

    # print(f"{name}: , position: ({position_X:.4E}, {position_Y:.4E}), velocity: ({velocity_X:.4E}, {velocity_Y:.4E})"
    #      f", mass: {mass_planet}")

    # print output
    print(f"{position_X:.4E} {position_Y:.4E} {velocity_X:.4E} {velocity_Y:.4E} {mass_planet}")
print(f"The sun's position, mass, and velocity did not change")
