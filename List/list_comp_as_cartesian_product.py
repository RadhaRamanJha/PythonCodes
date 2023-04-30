# Think About it more automatic contorl can be brought here i am sure
colors = ['Red','Yellow','Green','White','Black','Brown','Cyan','Magenta']
sizes = ['S','M','L','XL','XXL','XXXL']

# T-shirts arranged by color
print("T-shirt Available at Shop arranged by color")
# Database of T-shirts arranged by color
tshirt = [(color,size) for color in colors for size in sizes]

print("\n\t\t\t Presenting Red Color tshirt available")
print(tshirt[:6])
print("\n\t\t\t Presenting Yellow Color tshirt available")
print(tshirt[7:12])
print("\n\t\t\t Presenting Green Color tshirt available")
print(tshirt[13:18])
print("\n\t\t\t Presenting White Color tshirt available")
print(tshirt[19:24])
print("\n\t\t\t Presenting Black Color tshirt available")
print(tshirt[25:30])
print("\n\t\t\t Presenting Brown Color tshirt available")
print(tshirt[31:36])
print("\n\t\t\t Presenting Cyan Color tshirt available")
print(tshirt[37:42])
print("\n\t\t Presenting Magenta Color tshirt available")
print(tshirt[-6:])
# T-shirts arranged by size
print("\n\nT-shirt Available at Shop arranged by size")

# Database of T-shirts arranged by color
tshirt = [(size,color) for size in sizes for color in colors]
print("\n\t\t\t Presenting S-sized T-shirt")
print(tshirt[:8])
print("\n\t\t\t Presenting M-sized T-shirt")
print(tshirt[9:16])
print("\n\t\t\t Presenting L-sized T-shirt")
print(tshirt[17:24])
print("\n\t\t\t Presenting XL-sized T-shirt")
print(tshirt[25:32])
print("\n\t\t\t Presenting XXL-sized T-shirt")
print(tshirt[33:40])
print("\n\t\t\t Presenting XXXL-sized T-shirt")
print(tshirt[-8:])
