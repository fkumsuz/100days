from flask import Flask, render_template
import random
from datetime import datetime
import requests
# Get the current year

app = Flask(__name__)
gender_api= "https://api.genderize.io/"
age_api= "https://api.agify.io"

@app.route('/')  
def home():
    return render_template("index.html" )

@app.route('/<username>')
def name(username):
<<<<<<< HEAD
    gender_url= f"https://api.genderize.io?name={username}"
    age_url= f"https://api.agify.io?name={username}"
    username=username.capitalize()
    response_age = requests.get(age_url)
    age_data = response_age.json()
    age = age_data["age"]
    
    response_gender = requests.get(gender_url)
    gender_data = response_gender.json()
    gender = gender_data["gender"]  
    
    # response_age = requests.get(age_api, params={"name": name})
    # response_gender = requests.get(gender_api, params={"name": name})
=======
    gender_api= "https://api.genderize.io/"
    age_api= "https://api.agify.io"  
    response_age = requests.get(age_api, params={"name": name})
    response_gender = requests.get(gender_api, params={"name": name})
    if response_age.status_code == 200:
    # Parse the JSON response
        data = response_age.json()
        age = data.get("age")
    if response_gender.status_code == 200:
    # Parse the JSON response
        data = response_gender.json()
        gender = data.get("gender")
>>>>>>> 0d293f252c30fcc9324cb5e9c7823ab8f40ee0be
 
    return render_template("index.html",person_name=username,gender=gender,age=age)

if __name__ == "__main__":
    app.run(debug=True)


