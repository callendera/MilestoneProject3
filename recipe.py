import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
#sets up application for use with PyMongo, Flask

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'from_scratch'
#creates link between Database and application
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

#creates application to be tested

mongo = PyMongo(app)

@app.route('/')

@app.route('/add_recipes')
def add_recipes():
    from_scratch = mongo.db.myRecipes.find()
    return render_template( "addrecipes.html")

@app.route('/get_recipes')
#Display text as proof of concept
def get_recipes():
    from_scratch = mongo.db.recipes.find()
    return render_template( "recipes.html", from_scratch=from_scratch) 



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
#So they know how and where to run application