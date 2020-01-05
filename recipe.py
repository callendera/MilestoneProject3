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

#from_scratch is my database, recipes is my collection within the database

@app.route('/get_recipes')
#function used to display recipes on home page
def get_recipes():
    from_scratch = mongo.db.recipes.aggregate([{ "$sample": { "size": 4 } }])
    return render_template( "recipehome.html", from_scratch=from_scratch)

@app.route('/all_recipes')
#function used to display all recipes on All recipes page
def all_recipes():
    from_scratch = mongo.db.recipes.find()
    return render_template( "allrecipes.html", from_scratch=from_scratch)

@app.route('/add_recipes')
#function that triggers the modal and insert_recipe function
def add_recipes():
    return render_template("recipehome.html", recipe_types=mongo.db.recipe_types.find())
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    from_scratch = mongo.db.recipes
    recipes = from_scratch.insert(request.form.to_dict())
    #after adding the recipe to the database it redirects the user to the newly added recipe to view the full recipe
    return redirect(url_for('view_recipe', recipe_id=recipes))

@app.route('/view_recipe/<recipe_id>')
#function allows user to view the recipe details page, displays full recipe
def view_recipe(recipe_id):
    return render_template('recipedetails.html', from_scratch=mongo.db.recipes.find({'_id': ObjectId(recipe_id)}))
    

@app.route('/edit_recipe/<recipe_id>')
#function that triggers the edit recipe page, must call on particular Object id to trigger specific item in database
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('editrecipe.html', recipes=the_recipe)     

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
#function that allows the user to update the recipe in the database, must call on particular Object id to trigger specific item in database
def update_recipe(recipe_id):
    from_scratch = mongo.db.recipes
    recipes = from_scratch.update( {'_id': ObjectId(recipe_id)},
    {
        #gives the specifics of what is being updated below
        'recipe_name':request.form.get('recipe_name'),
        'recipe_type':request.form.get('recipe_type'),
        'ingredients0': request.form.get('ingredients0'),
        'directions0': request.form.get('directions0'),
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
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('all_recipes'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
#how and where to run application


