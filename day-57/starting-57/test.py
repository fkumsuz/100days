from flask import Flask, render_template
import random
import datetime
import requests

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_posts = response.json()

for blog_post in all_posts:
    print(blog_post )

 