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
 
    return render_template("index.html",person_name=username,gender=gender,age=age)

if __name__ == "__main__":
    app.run(debug=True)


