# Import the requests and json modules
import requests
import json

for i in range(11, 12):
    # Define the URL of the API endpoint
    url = f"https://api.gios.gov.pl/pjp-api/v1/rest/station/findAll?page={i}"

    # Make a GET request to the URL and store the response
    response = requests.get(url)

    # Check if the response status code is OK (200)
    if response.ok:
        # Parse the response content as JSON and store it as a dictionary
        data = response.json()
        # Open a file with the name 'data.json' and the mode 'w'
        with open(f'{i}.json', 'w') as f:
            # Write the JSON data to the file
            json.dump(data, f)
    else:
        # Handle the error if the response status code is not OK
        print(f"An error occurred: {response.status_code}")