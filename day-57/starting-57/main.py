from flask import Flask, render_template
import random
import datetime
import requests


app = Flask(__name__)

@app.route('/')
def home(): 
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html",posts=all_posts)

 
 
if __name__ == "__main__":
    app.run(debug=True)
