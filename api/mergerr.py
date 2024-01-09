import json

# Initialize an empty list to store all the data
all_data = []

# Loop over the file numbers
for i in range(16):
    # Open the file with UTF-8 encoding
    with open(f'{i}.json', 'r', encoding='utf-8') as f:
        # Load the JSON data from the file
        data = json.load(f)
        # Extract the "Lista stacji pomiarowych" data
        lista_stacji_pomiarowych = data.get('Lista stacji pomiarowych', [])
        # Add the data to the list
        all_data.extend(lista_stacji_pomiarowych)

# Write all the data to a new JSON file
with open('output.json', 'w') as f:
    json.dump(all_data, f)