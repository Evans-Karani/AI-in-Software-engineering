# Write a Python function to sort a list of dictionaries aby a given key.
def sort_dicts_by_key(dicts, key):
    """
    Sort a list of dictionaries by a given key.

    Parameters:
    dicts (list): A list of dictionaries to be sorted.
    key (str): The key by which to sort the dictionaries.

    Returns:
    list: A new list of dictionaries sorted by the specified key.
    """
    return sorted(dicts, key=lambda x: x[key])
def manual_sort_dicts_by_key(dicts, key):
    new_list = []
    while dicts:
        smallest = dicts[0]
        for item in dicts:
            if item[key] < smallest[key]:
                smallest = item
        new_list.append(smallest)
        dicts.remove(smallest)
    return new_list
sample_data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

print("AI Copilot Version:")
print(sort_dicts_by_key(sample_data.copy(), "age"))

print("\nManual Version:")
print(manual_sort_dicts_by_key(sample_data.copy(), "age"))

    