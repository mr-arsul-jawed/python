list = []
print(f"The initially list : list")

list.insert(0,"Aliah")
list.insert(1,"University")
print("After insertion:",list)

list.remove("University")
print("After remove operation: ",list)

list.append("University")
print("After appending operation: ",list)

print("Length of the list: ", len(list))

element=list.pop(1)
print("Removed element is :", element)

list.clear()
print("After clearing the list: ", list)