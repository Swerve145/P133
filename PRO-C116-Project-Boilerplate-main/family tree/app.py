# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Sahi" 
    age = "15"

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():
    return render_template('father.html')

# define the route to mother webpage
@app.route("/mother")
def mother():
    return render_template('mother.html')


# define the route to friends webpage
@app.route("/friends")
def friends():
    return render_template('friends.html')



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
