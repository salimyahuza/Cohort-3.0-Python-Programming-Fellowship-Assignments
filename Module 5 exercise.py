# Exercise level one

# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
items_list = [1, 2, 3, 4, 5, 6]

# Find the length of your list
length_of_list = len(items_list)
print(length_of_list)

# Get the first item, the middle item, and the last item of the list
first_item = items_list[0]
middle_item = items_list[len(items_list) // 2]
last_item = items_list[-1]
print(first_item, middle_item, last_item)

# Declare a list called mixed_data_types, put your name, age, height, marital status, address
mixed_data_types = ["Your Name", 25, 5.9, "Single", "Your Address"]

# Declare a list variable named it_companies and assign initial values
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle, and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]
print(first_company, middle_company, last_company)

# Print the list after modifying one of the companies
it_companies[0] = "Meta"
print(it_companies)

# Add an IT company to it_companies
it_companies.append("Tesla")
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, "Twitter")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# Join the it_companies with a string '#; '
joined_companies = ' #; '.join(it_companies)
print(joined_companies)

# Check if a certain company exists in the it_companies list
company_exists = "Google" in it_companies
print(company_exists)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
first_three_companies = it_companies[:3]
print(first_three_companies)

# Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]
print(last_three_companies)

# Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    middle_companies = it_companies[middle_index - 1:middle_index + 1]
else:
    middle_companies = it_companies[middle_index]
print(middle_companies)

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies from the list
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    del it_companies[middle_index - 1:middle_index + 1]
else:
    del it_companies[middle_index]
print(it_companies)

# Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux
full_stack = front_end + back_end
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)

#Exercise level two

# List of ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f"Sorted ages: {ages}")
print(f"Min age: {min_age}")
print(f"Max age: {max_age}")

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(f"Ages after adding min and max again: {ages}")

# Find the median age
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median_age = ages[n//2]
print(f"Median age: {median_age}")

# Find the average age
average_age = sum(ages) / n
print(f"Average age: {average_age}")

# Find the range of the ages
age_range = max_age - min_age
print(f"Age range: {age_range}")

# Compare the value of (min - average) and (max - average), use abs() method
min_average_diff = abs(min_age - average_age)
max_average_diff = abs(max_age - average_age)
print(f"Min - Average difference: {min_average_diff}")
print(f"Max - Average difference: {max_average_diff}")

# Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
n_countries = len(countries)
if n_countries % 2 == 0:
    middle_countries = countries[n_countries//2 - 1:n_countries//2 + 1]
else:
    middle_countries = [countries[n_countries//2]]
print(f"Middle country(ies): {middle_countries}")

# Divide the countries list into two equal lists if it is even if not one more country for the first half
first_half = countries[:(n_countries + 1) // 2]
second_half = countries[(n_countries + 1) // 2:]
print(f"First half: {first_half}")
print(f"Second half: {second_half}")

# Unpack the first three countries and the rest as scandic countries
first_three, *scandic_countries = countries[:3], countries[3:]
print(f"First three countries: {first_three}")
print(f"Scandic countries: {scandic_countries}")

# Tuple Exercises

# Level one exercise
# Create an empty tuple
empty_tuple = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ("Anna", "Bella")
brothers = ("John", "Mike")

# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings)

# How many siblings do you have?
number_of_siblings = len(siblings)
print(number_of_siblings)

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ("Father", "Mother")
print(family_members)

# Level two exercise

# Unpack siblings and parents from family_members
family_members = ("Anna", "Bella", "John", "Mike", "Father", "Mother")
siblings = family_members[:4]
parents = family_members[4:]
print(f"Siblings: {siblings}")
print(f"Parents: {parents}")

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp
fruits = ("Apple", "Banana", "Orange")
vegetables = ("Carrot", "Broccoli", "Spinach")
animal_products = ("Milk", "Eggs", "Cheese")
food_stuff_tp = fruits + vegetables + animal_products
print(f"Food stuff tuple: {food_stuff_tp}")

# Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(f"Food stuff list: {food_stuff_lt}")

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
n_food = len(food_stuff_lt)
if n_food % 2 == 0:
    middle_items = food_stuff_lt[n_food//2 - 1:n_food//2 + 1]
else:
    middle_items = [food_stuff_lt[n_food//2]]
print(f"Middle item(s): {middle_items}")

# Slice out the first three items and the last three items from food_stuff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print(f"First three items: {first_three_items}")
print(f"Last three items: {last_three_items}")

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple
# Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
is_estonia_nordic = 'Estonia' in nordic_countries
print(f"Is Estonia a nordic country? {is_estonia_nordic}")

# Check if 'Iceland' is a nordic country
is_iceland_nordic = 'Iceland' in nordic_countries
print(f"Is Iceland a nordic country? {is_iceland_nordic}")

# Sets Exercises

# Sets Exercises: Level 1
# Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
length_it_companies = len(it_companies)
print(f"Length of it_companies: {length_it_companies}")

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(f"it_companies after adding Twitter: {it_companies}")

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Tesla', 'SpaceX', 'Netflix'])
print(f"it_companies after adding multiple companies: {it_companies}")

# Remove one of the companies from the set it_companies
it_companies.remove('Facebook')
print(f"it_companies after removing Facebook: {it_companies}")

The difference between remove and discard:
The remove() method will raise a KeyError if the item does not exist in the set.
The discard() method will not raise an error if the item does not exist.

# Sets Exercises: Level 2
# Joining A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A_union_B = A.union(B)
print(f"A union B: {A_union_B}")

# Finding the intersection of A and B
A_intersection_B = A.intersection(B)
print(f"A intersection B: {A_intersection_B}")

# Checking whether or not A is a subset of B
is_A_subset_B = A.issubset(B)
print(f"Is A subset of B: {is_A_subset_B}")

# Checking whether or not A and B disjoint sets
are_A_B_disjoint = A.isdisjoint(B)
print(f"Are A and B disjoint sets: {are_A_B_disjoint}")

# Joining A with B and B with A
A_join_B = A.union(B)
B_join_A = B.union(A)
print(f"A join B: {A_join_B}")
print(f"B join A: {B_join_A}")

# Symmetric difference between A and B
A_symmetric_difference_B = A.symmetric_difference(B)
print(f"Symmetric difference between A and B: {A_symmetric_difference_B}")

# Deleting the sets completely
del A
del B

# Sets Exercises: Level 3
# Converting the ages to a set and comparing the length of the list and the set
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
length_age_list = len(age)
length_age_set = len(age_set)
print(f"Length of age list: {length_age_list}")
print(f"Length of age set: {length_age_set}")
if length_age_list > length_age_set:
    print("The list is bigger.")
else:
    print("The set is bigger.")

# Explaining the difference between string, list, tuple and set
data_type_explanation = """
- String: An immutable sequence of characters.
- List: An ordered collection of items that is mutable.
- Tuple: An ordered collection of items that is immutable.
- Set: An unordered collection of unique items that is mutable.
"""
print(data_type_explanation)

# Unique words that have been used in the sentence and using the split methods and set to get the unique words
sentence = "I am a teacher and I love to inspire and teach people."
unique_words = set(sentence.split())
number_of_unique_words = len(unique_words)
print(f"Number of unique words in the sentence: {number_of_unique_words}")

