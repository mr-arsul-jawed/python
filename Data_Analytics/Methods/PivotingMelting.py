# Example of Pivoting in Pandas
# import pandas as pd

# dict = {
#         "keys": ["k1","k2","k1","k2"],
#         "Name": ["Alice", "Bob", "Charlie", "David"],
#         "House": ["Red", "Blue", "Green", "Yellow"],
#         "Grade": ["3rd", "4th", "5th", "6th"]
#         }

# df = pd.DataFrame(dict)
# # print("Original DataFrame:")
# # print(df)
# print(df.pivot(index='keys', columns='Name', values=['House']))
# print(df.pivot(index='keys', columns='Name', values=['House', 'Grade']))
# # print(df.pivot("keys", "Names", "Houses")) # This will give error as there are duplicate entries for k1 and k2

# Example of Melting in Pandas
# import pandas as pd

# dict = {
#         "Name": ["Alice", "Bob", "Charlie", "David"],
#         "House": ["Red", "Blue", "Green", "Yellow"],
#         "Grade": ["3rd", "4th", "5th", "6th"]
#         }


# df = pd.DataFrame(dict)
# print(df)

# # melted_df = pd.melt(df, id_vars=["Name"], value_vars=["House"], var_name="House", value_name="House Color")
# melted_df = pd.melt(df, id_vars=["Name"], value_vars=["House","Grade"], var_name="House & Grade", value_name="Value")
# print("\nMelted DataFrame:")
# print(melted_df)

