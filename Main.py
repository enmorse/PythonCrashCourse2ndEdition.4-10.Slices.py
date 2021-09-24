# Use a list comprehension to generate a list of the first
# 10 cubes.

cubes = [value ** 3 for value in range(1, 10)]

print(cubes)

# Using one of the programs you wrote in this chapter,
# add several lines to the end of the program that do
# the following:
# Print the message "The first three items in the list are: ".
# Then use a slice to print the first three items from that
# program's list.

values_in_cubes = "The first three items in the list are: "

print(f"{values_in_cubes}", cubes[0:3])

# Print the message "Three items from the middle of the
# list are: ". Use a slice to print three items from the
# middle of the list.

values_in_cubes1 = "Three items from the middle of " \
                   "the list are: "

print(f"{values_in_cubes1}", cubes[3:6])

# Print the message "The last three items in the list are: ".
# Use a slice to print the last three items in the list.

values_in_cubes = "The last three items in the list are: "

print(f"{values_in_cubes}", cubes[6:9])

print(f"{values_in_cubes}", cubes[-3:])
