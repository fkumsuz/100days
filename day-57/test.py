import requests

# Define the API endpoint
age_api = "https://api.agify.io"

# Input name for which you want to predict age
name = "John"

# Make a GET request to the API with the name parameter
response = requests.get(age_api, params={"name": name})

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Extract the predicted age
    age = data.get("age")
    
    # Print the predicted age
    print(f"The predicted age for the name '{name}' is: {age}")
else:
    print("Error:", response.status_code)
