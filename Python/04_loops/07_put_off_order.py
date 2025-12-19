flavors = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]


for flavor in flavors:
    if flavor == 'Out of Stock':
        continue
    if flavor == 'Discontinued':
        print("{flavor} item found")
        break
    print("{flavor} item found")
    
    
print("Outside of loop")