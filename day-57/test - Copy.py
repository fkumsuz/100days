import requests

# Define the API endpoint
age_api = "https://api.agify.io"
gender_api= "https://api.genderize.io/"

# Input name for which you want to predict age
name = "John"

# Make a GET request to the API with the name parameter
response = requests.get(age_api, params={"name": name})
response_age = requests.get(age_api, params={"name": name})
response_gender = requests.get(gender_api, params={"name": name})
# Check if the request was successful (status code 200)
if response_age.status_code == 200:
    # Parse the JSON response
    data = response_age.json()
    age = data.get("age")
if response_gender.status_code == 200:
    # Parse the JSON response
    data = response_gender.json()
    gender = data.get("gender")
    
    # Print the predicted age
    print(f"The predicted age for the name '{name}' is: {age} and gender is : {gender}")
else:
    print("Error:", response.status_code)
