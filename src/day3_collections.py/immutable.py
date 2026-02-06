# Create a tuple for screen resolution
screen_res = (1920, 1080)

# Print the current resolution
print("Current Resolution: 1920x1080")

# The Experiment (this line causes a TypeError if uncommented)
# screen_res[0] = 1280

# The Fix
print("Tuples cannot be modified!")
