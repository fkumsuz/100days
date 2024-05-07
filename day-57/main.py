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
    gender="male"
    age=24
    return render_template("index.html",gender=gender,age=age)

@app.route('/<username>')
def name(username):
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
 
    return render_template("index.html",username=username,gender=gender,age=age)

if __name__ == "__main__":
    app.run(debug=True)


