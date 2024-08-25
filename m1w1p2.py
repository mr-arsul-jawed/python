dict = {"A" : "Aliah","U" : "University"}
print("Print items :", dict.items())

print("Access item  by key \"A\" :", dict["A"])

print("key \"U\" using get() :", dict.get("U"))

dict.update({"U": "Universal"})
print("After update, access item \"U\" : ", dict["U"])

print("Length of the dictionary :", len(dict))