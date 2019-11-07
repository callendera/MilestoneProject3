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

@app.route('/get_recipes')
#Display text as proof of concept
def get_recipes():
    from_scratch = mongo.db.recipes.find()
    return render_template( "recipehome.html", from_scratch=from_scratch) 

@app.route('/add_recipes')
def add_recipes():
    from_scratch = mongo.db.recipes.find()
    return render_template("recipehome.html")

@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    return render_template('recipedetails.html', from_scratch=mongo.db.recipes.find({'_id': ObjectId(recipe_id)}))
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    from_scratch = mongo.db.recipes
    recipes = from_scratch.insert(request.form.to_dict())
    return redirect(url_for('view_recipe', recipe_id=recipes))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('editrecipe.html', recipes=the_recipe)     

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    from_scratch = mongo.db.recipes
    from_scratch.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'recipe_type':request.form.get('recipe_type'),
        'ingredients0': request.form.get('ingredients0'),
        'directions0': request.form.get('directions0'),
        'nutrition0':request.form.get('nutrition0'),
        'serves':request.form.get('serves'),
        'recipe_by':request.form.get('recipe_by'),
        'recipe_image':request.form.get('recipe_image')
    })
    return redirect('get_recipes')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
#So they know how and where to run application


