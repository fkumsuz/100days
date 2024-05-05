import random
from flask import Flask
 
app = Flask(__name__)

 

high="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
low="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
correct="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"

  
@app.route('/')
def index():
    return '<h1>Guess a number between 0 and 9<h1>'\
        '<img src= "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

random_number = random.randint(0, 9)  
@app.route('/<int:number>')   
def home(number): 
    global random_number
    if number > random_number:
        value = '<h1 style="color:red;">Too high,try again!</h1>'\
        f'<img src={high} width=500 height=500>'
 
    
    elif number < random_number:
        value = '<h1 style="color:purple;">Too low,try again!</h1>'\
        f'<img src={low} width=500 height=500>'
    else:
        value = '<h1 style="color:green;" >You found me!<h1>'\
        f'<img src={correct} width=500 height=500>'
    return value
   
                     

if __name__ == '__main__':
    app.run(debug=True)