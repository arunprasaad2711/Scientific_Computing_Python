'''

else, Break, continue, pass

'''

for i in range(0, 10, 1):
	print(i)
else:
	print("iterating values are over!")

l1 = ["Hydrogen", "Helium", "Lithium"]

for element in l1:
	print(element)
	if element == "Helium":
		print("Encountered Helium!")
		break

for element in l1:

	if element == "Helium":
		print("Encountered Helium! So, skipping!")
		continue
	else:
		print(element)

	print(f"Iteration over with {element}")

for element in l1:
	pass

