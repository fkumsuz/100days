from flask import Flask

# @make_bold
# @make_emphasis
# @make_underlined


def make_bold(function):
    def wrapper_function(): 
        value = function()
        value = "<b>"+value+"</b>"
        return value
    return wrapper_function

def make_emphasis(function):
    def wrapper_function(): 
        value = function()
        value = "<em>"+value+"</em>"
        return value
    return wrapper_function

def make_underlined(function):
    def wrapper_function(): 
        value = function()
        value = "<u>"+value+"</u>"
        return value
    return wrapper_function

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/bye')
@make_bold
@make_underlined
@make_emphasis
def bye():
    return 'Bye!'  

@app.route('/<username>/<int:number>')
def greet(username,number):
    return f'<h1>Hello {username} there {number}!</h1>'\
        '<p>This is a paragraph.</p>'\
        '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExazUwbmJ0OXpiZ3RtcWNheXQ2eTh4dmhjdnFzNWJjYTN1cDc1eHVmbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/BRwgvFM9BfP8c/giphy.gif" width=500 height=500>'
            

if __name__ == '__main__':
    app.run(debug=True)