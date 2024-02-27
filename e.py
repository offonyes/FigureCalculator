import math

a = 3
b = 4
c = 5

# Calculate angle A in degrees
angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))

# Calculate x-coordinate of point B
b_coords = b * math.cos(math.radians(angle_A))

print(f"The x-coordinate of point B is approximately: {b_coords}")
