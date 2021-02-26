'''
Some instructions:
1. Documentation
   Here's a Tutorial for Flask:
    https://pythonspot.com/flask-hello-world/

2. First install flask (you'll only have to do this once):
   Note that before you begin, you will have to 
   install flask on the command line as follows:
     pip3 install flask

3. Running this file will start a web server.
   To actually execute the code, open your web browser
   and navigate to: http://127.0.0.1:5000/ 

4. If you actually want to turn this into a website, read the
   PythonAnywhere documentation, which teaches you how to upload
   your files so that you can serve them as a web page.

'''

from flask import Flask
app = Flask(__name__)
import random
    
photos = [
    'static/kittens.jpg',
    'static/beagle-puppy.jpg',
    'static/kangaroo.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/1/18/Vombatus_ursinus_-Maria_Island_National_Park.jpg'
]

@app.route("/")
def home():
    # this page's job is to pick a random photo from a list
    return '<img src="{0}" />'.format(random.choice(photos))

@app.route("/tuesday")
def reminder1():
    return "Drinking water is a good thing to do."

@app.route("/wednesday")
def reminder2():
    return "Don't forget to eat your vegetables"

@app.route("/friday")
def friday_page():
    # Update the Friday function so that it returns an HTML page
    # using the string's format method. Take a look at the html_samples
    # folder for ideas.
    return "TODO"

if __name__ == "__main__":
    app.run()