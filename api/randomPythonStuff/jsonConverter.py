import json

# Open the JSON file
with open('ludnosc.json', 'r', encoding='utf-8') as f:
    # Load the JSON data
    data = json.load(f)

# Iterate over the objects in the data
for obj in data:
    # Convert the "lud_1_km2" string to a float
    obj['lud_1_km2'] = float(obj['lud_1_km2'].replace(' ','').replace(',', '.'))
    # Convert the "ter_woj" and "ter_pow" strings to integers
    obj['ter_woj'] = int(obj['ter_woj'])
    obj['ter_pow'] = int(obj['ter_pow'])

# Open the JSON file for writing
with open('csvjson.json', 'w', encoding='utf-8') as f:
    # Write the updated data to the file
    json.dump(data, f, ensure_ascii=False, indent=4)