"""This program is used to complete CRUD and display recipes within the site.

All function names outline the particular usage of the each function. Whereas, 
all_recipes will display all of the recipes within the database. The insert_recipe 
function inserts the recipe into the database. Each function also has comments 
to describe what the specific functionality is. The functions are used to Create (add and insert functions) recipes,
Read recipes (view and all recipe functions), Update recipes (edit and update recipe functions), and Delete recipes(delete recipe function). 
The function get_recipes then displays recipehome.html. 

The use of render_template is used to trigger specific functions to display those html files.
Redirect helps to show the user the recipe they just add, updated, or sends user to home page after deleting a recipe.
"""

import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
#sets up application for use with PyMongo, Flask, Bson file, and OS for the underlying operating system python is running on

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'from_scratch'
#creates link between Database and application
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

@app.route('/')

#from_scratch is my database, recipes and types are my collections within the database

@app.route('/get_recipes')
#function used to display recipes on home page
def get_recipes():
    from_scratch = mongo.db.recipes.aggregate([{ "$sample": { "size": 4 } }])
    return render_template( "recipehome.html", from_scratch=from_scratch, types=mongo.db.types.find())

@app.route('/all_recipes')
#function used to display all recipes on All recipes page
def all_recipes():
    from_scratch = mongo.db.recipes.find()
    return render_template( "allrecipes.html", from_scratch=from_scratch, types=mongo.db.types.find())

@app.route('/add_recipes')
#function that triggers the modal and insert_recipe function
def add_recipes():
    return render_template("recipehome.html", types=mongo.db.types.find())
    
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    new_recipe = request.form.to_dict()
    # for loop with if statement prevents user from submitting a blank form with only space characters
    for field in new_recipe:
        if new_recipe[field].isspace() == True:
            return render_template('error_addrecipe.html', types=mongo.db.types.find())
    recipes = mongo.db.recipes.insert(new_recipe)
    #after adding the recipe to the database it redirects the user to the newly added recipe to view the full recipe
    return redirect(url_for('view_recipe', recipe_id=recipes))


@app.route('/view_recipe/<recipe_id>')
#function allows user to view the recipe details page, displays full recipe
def view_recipe(recipe_id):
    return render_template('recipedetails.html', types=mongo.db.types.find(), from_scratch=mongo.db.recipes.find({'_id': ObjectId(recipe_id)}))
    

@app.route('/edit_recipe/<recipe_id>')
#function that triggers the edit recipe page, must call on particular Object id to trigger specific item in database
def edit_recipe(recipe_id):
    recipes =  mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    if recipes['recipe_by'].lower() == 'admin':
        return render_template('error_recipedetails.html', types=mongo.db.types.find(), from_scratch=mongo.db.recipes.find({'_id': ObjectId(recipe_id)})) 
    the_recipe =  mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('editrecipe.html', recipes=the_recipe, types=mongo.db.types.find())     

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
#function that allows the user to update the recipe in the database, must call on particular Object id to trigger specific item in database
def update_recipe(recipe_id):
    from_scratch = mongo.db.recipes
    the_recipe =  mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    recipe_name = request.form.get('recipe_name')
    ingredients = request.form.get('ingredients0')
    directions = request.form.get('directions0')
    nutrition = request.form.get('nutrition0')
    recipe_by = request.form.get('recipe_by')
    recipe_image = request.form.get('recipe_image')
    # The following IF statements run a check on the following inputs to not allow the user to enter a blank space, tab space, or any space characters
    if recipe_name.isspace() == True:
        return render_template('error_editrecipe.html', recipes=the_recipe, types=mongo.db.types.find())
    if ingredients.isspace() == True:
        return render_template('error_editrecipe.html', recipes=the_recipe, types=mongo.db.types.find())
    if directions.isspace() == True:
        return render_template('error_editrecipe.html', recipes=the_recipe, types=mongo.db.types.find())
    if nutrition.isspace() == True:
        return render_template('error_editrecipe.html', recipes=the_recipe, types=mongo.db.types.find())
    if recipe_by.isspace() == True:
        return render_template('error_editrecipe.html', recipes=the_recipe, types=mongo.db.types.find())
    if recipe_image.isspace() == True:
        return render_template('error_editrecipe.html', recipes=the_recipe, types=mongo.db.types.find())

    recipes = from_scratch.update( {'_id': ObjectId(recipe_id)},
    { #gives the specifics of what is being updated below
        'recipe_name':request.form.get('recipe_name'),
        'type':request.form.get('type'),
        'ingredients0':request.form.get('ingredients0'),
        'directions0':request.form.get('directions0'),
        'nutrition0':request.form.get('nutrition0'),
        'serves':request.form.get('serves'),
        'recipe_by':request.form.get('recipe_by'),  
        'recipe_image':request.form.get('recipe_image')
    })
    #after updating the recipe it redirects the user to the now updated recipe
    return redirect(url_for('view_recipe', recipe_id=recipe_id))
    
@app.route('/delete_recipe/<recipe_id>')
#function located in the modal to delete the recipe
def delete_recipe(recipe_id):
    recipes =  mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    if recipes['recipe_by'].lower() == 'admin':
        return render_template('error_recipedetails.html', types=mongo.db.types.find(), from_scratch=mongo.db.recipes.find({'_id': ObjectId(recipe_id)})) 
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('all_recipes'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
#how and where to run application


