import json

# Open the JSON file
with open('bases.json', 'r', encoding='utf-8') as f:
    # Load the JSON data
    data = json.load(f)

# Print the data
print(data)