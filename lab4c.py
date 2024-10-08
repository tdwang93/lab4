#!/usr/bin/env python3

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

# Function to create a dictionary from two lists (keys and values)
def create_dictionary(keys, values):
    # Initialize an empty dictionary
    new_dict = {}
    # Use a while loop to combine keys and values into the dictionary
    i = 0
    while i < len(keys) and i < len(values):
        new_dict[keys[i]] = values[i]
        i += 1
    return new_dict

# Function to find shared values between two dictionaries
def shared_values(dict1, dict2):
    # Extract the sets of values from both dictionaries
    set1 = set(dict1.values())
    set2 = set(dict2.values())
    # Return the intersection (common values)
    return set1 & set2

# Main block to test the functions
if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values:', common)
