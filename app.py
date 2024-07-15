# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Oviya" # write your name
    age = "13" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():
    name = "Mitul"
    age = "46"
    return render_template("father.html")
# define the route to mother webpage
@app.route("/mother")
def mother():
    name = "Aarti"
    age = "45"
    return render_template("mother.html")
# define the route to friends webpage
@app.route("/friend")
def friend():
    name = "Ishani"
    age = "14"
    return render_template("friend.html")
# add other routes, if you want
@app.route("/brother")
def brother():
    name = "Atharv"
    age = "15"
    return render_template("brother.html")
# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
