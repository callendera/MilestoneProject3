# Milestone Project 3: Data Centric Developement
## Check out App Deployed on Heroku [here](https://from-scratch-recipe-app.herokuapp.com/)
## Objective
The From Scratch app was designed to connect my extended family by shareing recipes. Our family is grounded and built, not only on shareing meals, but shareing memories. The 
importance within my family to share recipes is less of a way to simply share recipes, it is a way for us to connect. From our family to all families, 
food is a great way to connect with eachother.
My 3rd Milestone Project is an app for my family to share old family recipes. This project displays the skills learned in the modules leading up to this project including:
HTML Fundamentals, CSS Fundamentals, JavaScript, Interactive Frontend Developement, Python, and Data Centric Developement.
By adding Python and Data Centric Developement to my skill set, I have added to the ability for the user to Create, Update, Edit, and Delete recipes within the app. 
Not only does the app have excellent UX, but it allows the user to share their favorite recipes with the entire family.
## Project Description and UX
The goal of this app is to provide a place where users can:
* Browse Recipes
* Add Recipes
* Edit/Update Recipes
* Delete recipes

The UX of the app was designed in a way to provide easy access and simplicity. While keeping in mind the older generations within my family, 
I wanted to develop an app that made it easy and simple for those generations to access on any device.

The app is fully functional on all screen sizes with extensive testing for each feature on 1400px, 1200px, 992px, 768px, and 576px screensizes.

* User Stories:
    * As a Family member interested in browsing the recipes, I visit the app and on the home page 4 featured recipes are displayed. 
    I use the Navbar and select the All Recipes option, I am directed to the page That has all of the recipes listed on it. 
    * If I am a user that is browsing the recipes and I find a recipe I am interested in, if I click on that recipe image, The app directs me to View the Full recipe. 
    That recipe is displayed with all of the appropriate Information about that recipe. 
    * If I am browsing a recipe and I view the full recipe, In the bottom right hand cornner is a button that allows me to hover it to get all the options for that recipe. 
    Within the button I can delete the recipe or edit the recipe.
        * Delete: The user who would like to delete the recipe can do so by clicking the trashcan option in the View recipe page. 
        From there a modal opens to ask the user if they are sure They would like to delete. After the user selects yes, to delete the user is redirected to the home page.
        If the recipe is one added by an 'Admin', the user is directed to an error page. The message at the top of the page reads: "recipes created by admin can not be deleted"
        * Edit: The user who would like to edit the recipe can do so by clicking the pencil option in the View recipe page. 
        From there, a new page is opened that allows the user to make edits to the Recipe.
        (If the recipe is created by the admin, the user is directed to an error page that reads "recipes created by admin can not be edited")
        Each field in the edit recipe form Is prefilled with the deatails of that particular 
        recipe to be edited. When the user has made the edits they would like to make, they will submit the form and be directed to view the recipe that was just edited in the View recipe page as an updated recipe.
        * Add: The user who would like to add a recipe may do so from the home page in the Navbar. If the user selects this option, 
        a modal is triggered that give the user all of the appropriate fields to submit the recipe to the app. 
        After the user submits the completed form the recipe is immediatly displayed in the View recipe page. This allows the user to look at the recipe just added.
        If the user inputs a value that is solely a space character, or not content, an error page will appear with a new form telling the user "You entered input with no content, please try again". 
        From there, the user can reenter the form in the correct manner. 

### Original Mockup
##### Everything changed tramendously from the original Mockup, I relied mostly on the Site Map (mockup images also available in static folder) 

![Original Mockup](https://i.ibb.co/4Vzkv17/thumbnail-private-var-mobile-Containers-Data-Application-EFC929-DA-8312-406-F-8-FE7-25-D56-F9915-F4-tmp-865-C6-E67-868-F-45-F9-9-CC2-8-CEA498-C9-FF3-Image-1.jpg)
 
### Site Map
 
 ![Site Map/Web](https://i.ibb.co/txb47BZ/thumbnail-private-var-mobile-Containers-Data-Application-EFC929-DA-8312-406-F-8-FE7-25-D56-F9915-F4-tmp-B82-EA8-F2-A798-47-F6-91-A4-1-D2-DDB07952-D-Image.jpg) 
 
## Features

### Existing Features
* Navbar 
    * Fixed to the top for easy navigation 
    * From Scratch Logo in left corner
    * Includes: Home|All Recipes|Add Recipe Each navigates you throughout the app
    * Navigation links become a toggler in the mobile veiw and smaller screen sizes with a Side Navbar with the same options
* Callout
    * Contains background and a breif description of what the app is. Also acts as a way to grab a user to get them to use the app
* List of all recipes
    * Avaliable when the user navigates using the navbar. Displays all recipes present in the database. 
* Modal #1
    * Gives a form for the user to add a recipe. ALL RECIPE FORMS IN THE APP ARE SET UP AS DESCRIBED BELOW, PLEASE REFER HERE WHEN REFERENCING THE STYLE/LAYOUT/BACKEND INFO BEHIND ALL FORMS.
    * Inputs are all required except for the Recipe Image URL and the Nutrition Facts. With it being a family forum, it seems off to require those fields. 
        * The select field allows the user to pick one of 6 categories, The field cannot be left blank, so no need to a backend validation
        * The Name, Ingredients, Directions, Nutrition Facts, Recipe By; are all required to send the form, but required backend validation to prevent the user from inputing blank content/space charaters.
            * If the user inputs values with no content for any of these fields, The app redirects the user to a new Add Recipe Form that explains to the user that input with no content Can Not be submitted to the Database.
        * The Serves: input is required, while also including a number input validation and the Min number can not be less than one, to work logically. 
        * The Recipe Image URL is not required, but if the user does input a URL a validation will be triggered to not submit the form without that input being a URL. If the user decides to leave that input blank, app generates a default image. 
* Modal #2 
    * Asks user if they are sure they would like to delete the recipe.
        * If the user hits yes, a backend check is ran on the recipe info to see if the recipe was added by the Admin or not. If the recipe was added by the Admin, the recipe can not be deleted.
            * In the case that the recipe was infact added by the Admin, the user will be redirected to a page that explains the error to the user. 
            * If the recipe was not created by an Admin, Then the recipe will be deleted and the user will be taken to the all recipes page to browse more recipes.
* Recipe Details View
    * After clicking the recipe image all of the recipe details are displayed on a new page. This page includes all of the details that are storred in the database about the recipe.
    * At the bottom right of the page, a Floating Action Button or FAB is there. This button pulses to show the user that it can be used. 
* Floating action button on View Recipe Details page.
    * This button pulsates to get user attention, when hovered the option to edit and delete the recipe are shown. EDIT directs to new page, DELETE toggles second modal
        * When the user clicks the edit button, a check is ran to see if the recipe was created by admin. If the recipe was created by the admin, the recipe can not be edited. 
        * The Edit Recipe page contains the form mentioned above with all the input fields filled with the information from the database for that specific recipe. The form has all the same validation that the add recipe form has. 

### Features left to Implement 
* Log In/Register
    * A feature I would like to implement with more time to gain the skills to use this feature.
    * This would also help with some validation issues. 
* Search Box
    * A feature I would like to implement with more time to gain the skills to use this feature. 
* Upload Recipe Images
    * Will learn in future modules, for now the user must copy and paste a URL for the image

## Tools/Technologies
* [AWS Cloud9](https://c9.io/login)
    * Cloud9 hosted my Workspace for this project
* [Git](https://git-scm.com/)
    * used to push and commit any and all changes to my repository on GitHub
* [Materialize](https://materializecss.com/)
    * Provided my buttons, modal, Navbar, and basic grid structure 
* [JQuery](https://jquery.com/)
    * The project uses JQuery for DOM manipulation (Ex: Modal)
* [JavaScript](https://www.javascript.com/)
    * Used along with Materialize for the modal, Floating action button, Side Navigation, and Select option within form in modal
* [MongoDB](https://www.mongodb.com)
    * stored my From Scratch database and recipes collection
* [Heroku](https://signup.heroku.com/t/platform?c=70130000001xDpdAAE&gclid=EAIaIQobChMI_ZvP4LXl5QIVEYzICh1T0g2FEAAYASAAEgIoQPD_BwE)
    * Deployment of my app From-Scratch
* [Flask](http://flask.palletsprojects.com/en/1.1.x/)
    * Debugging with Jinja, Flask app

## Testing
### Automated Testing
* Validation Services
    * [W3C Markup Validator](https://validator.w3.org/) was used to validate my HTML code.
    * [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS code.
    * [JSHint](https://jshint.com/) was used to test JS code.

### UX stories testing / Manual Testing
All features were tested on Google Chrome, Internet Explorer, and Firefox. Mobile/Tablet features were tested on Apple and Samsung devices. Everything was tested using a wide range of screensizes.
* As a user I want to:
    * Browse Recipes:
        * After coming to the home page,
        * click the all recipes button in navbar or scroll down the page 
        * On the home page the get_recipes is triggered to show the for loop of the 4 featured recipes on the home page. 
        * On the All recipes page the all_recipes function allows the for loop to display all of the recipes there as well. 
    * View Recipe details:
        * Upon browsing all the recipes,
        * click the recipe image
        * This triggers the view_recipe function that then directs you to the recipedetails.html page
        * On that page the full recipe and all details needed to make the recipe is included.
        
    * Add a Recipe
        * Come to the home page, use the add recipe option in the Navbar
        * This button triggers the add_recipe function, opens modal
            * The Modal that opens contains the form needed to add the recipe and for the user to give all the appropriate information.
            * Each form inputs are required, except for the Nutrition Facts and Recipe Image URL.
            * Input fields: Recipe Name | Recipe Type(with select scroll bar options) | Ingredients | Directions | Serves how many people? | Nutrition Facts | Recipe by; | and the Recipe Image URL input 
            * The user then submits the form triggering the insert_recipe function. This function inserts the new recipe into the mongodb database. A message appears that tells the user they can now view the recipe below, after hitting okay, the user is directed to the view recipe page of the newly added recipe.
            * If the user inputs all space charaters/empty content, The error page error_addrecipe.html is triggered through the insert_recipe function when it checks the input fields. This page displays an error message and provides a new form for the user to try again on. 
            
    * Edit a Recipe
        * While viewing the details of a recipe the user can update the recipe, if it is not a recipe created by an Admin.
        * hover over pulsating button (bottom right hand corner) to reveal the edit recipe option 
        * After clicking the edit recipe button (triggering the edit_recipe function), the user is directed to the editrecipe.html page:
            * This form is identical to the add recipe form, except the input fields are filled with the information matching the recipe to be updated
            * When the form is submitted it triggers the update_recipe function. This function changes the recipe based on the new user input.  A message appears that tells the user they can now view the updated recipe below, after hitting okay, the user is directed to the view recipe page of the newly updated recipe.
        * If the user tries to edit a recipe created by the Admin, They are then shown an error message upon clicking the edit recipe option in the Floating Action Button, this message is located in the error_recipedetails.html. This check is triggered by the edit_recipe function.
    * Delete a Recipe
        * While viewing the details of a recipe the user can delete the recipe
        * hover over pulsating button (bottom right hand corner) to reveal the delete recipe option
         * After clicking the delete recipe button it opens the confirm deletion modal:
            * The modal asks if the user is sure they would like to delete the seleted recipe,
            * If the user clicks the delete button the delete_recipe function is triggered and the user is directed back to the home page via the get_recipe function.
            * If the user tries to delete a recipe added by an admin, the recipe will not be deleted. In the delete_recipe function, there is a check for if the recipe was created by an admin. The user would be taken to the error_recipedetails.html page to explain the error.
            * If the user hits cancel, the modal closes.

### Logic and Functionality of Functions in recipe.py file 
##### The following is an in-depth description of each function and it's purpose:

```
@app.route('/get_recipes')
#function used to display recipes on home page
def get_recipes():
    from_scratch = mongo.db.recipes.aggregate([{ "$sample": { "size": 4 } }])
    return render_template( "recipehome.html", from_scratch=from_scratch, types=mongo.db.types.find())

```
* The get_recipes function renders the template recipehome.html
* It pulls from the from_scratch database collection recipes
* The `types=mongo.db.types.find()` is used as a parameter for render_template becuase this is a seperate collection within the database called types. It looks for the first occurance of the type in the types collection and iterates over it.
* The `.aggregate()` is used to compute all data types from the database so all of it can be used in these instances of a for-loop that may iterate over the database. 
* These recipes are a random 4 sample size from the database, and are highlighted in the app as the featured recipes on the Home page.

```
@app.route('/all_recipes')
#function used to display all recipes on All recipes page
def all_recipes():
    from_scratch = mongo.db.recipes.find()
    return render_template( "allrecipes.html", from_scratch=from_scratch, types=mongo.db.types.find())
```
* The all_recipes function does exactly that, displays all of the recipes from the database
* The `.find()` method is used here to find the 1st occurance a recipe in the from_scratch database and then iterate through the recipe collection in a for-loop 
* It renders the template allrecipes.html
* The `types=mongo.db.types.find()` is used as a parameter for render_template becuase this is a seperate collection within the database called types. It looks for the first occurance of the type in the types collection and iterates over it.

```
@app.route('/add_recipes')
#function that triggers the modal and insert_recipe function
def add_recipes():
    return render_template("recipehome.html", types=mongo.db.types.find())
```
* This function simply triggers the modal that contains the Add Recipe form (Modal #1). 
* The `types=mongo.db.types.find()` is used as a parameter for render_template becuase this is a seperate collection within the database called types. It looks for the first occurance of the type in the types collection and iterates over it.

```
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
```
* This function is triggered when a user hits the submit button in the Add Recipe form. 
* The method is POST because we want to send info retrieved from the form to the database
* I defined the variable `new_recipe = request.form.to.dict()`, to be able to check that any field in the new recipe contains only space characters. The If statements says that if the `.isspace() == True:` Then return the error_addrecipe.html template. 
* The above check is ran before the recipe is inserted into the database.
* The `.insert(new_recipe)` inserts the recipe into the database. 
* After the recipe is successfuly inserted into the database, The user is redirected in the return statement to the `redirect(url_for('view_recipe', recipe_id=recipes))`. This takes the user to view that specific recipe after they have added that recipe to view the recipe details.
* View_recipe is another function that renders the template recipedetails.html

```
@app.route('/view_recipe/<recipe_id>')
#function allows user to view the recipe details page, displays full recipe
def view_recipe(recipe_id):
    return render_template('recipedetails.html', types=mongo.db.types.find(), from_scratch=mongo.db.recipes.find({'_id': ObjectId(recipe_id)}))
```
* This function renders the recipedetails.html template.
* Also uses the recipe_id to reference a specific recipe thats is called to in the database.

```
@app.route('/edit_recipe/<recipe_id>')
#function that triggers the edit recipe page, must call on particular Object id to trigger specific item in database
def edit_recipe(recipe_id):
    recipes =  mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    if recipes['recipe_by'].lower() == 'admin':
        return render_template('error_recipedetails.html', types=mongo.db.types.find(), from_scratch=mongo.db.recipes.find({'_id': ObjectId(recipe_id)})) 
    the_recipe =  mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('editrecipe.html', recipes=the_recipe, types=mongo.db.types.find())
```
* This function triggers the editrecipe.html page of a specific recipe using the recipe ID
* In this function, I run a check using an IF statement to check if the recipe_by key is equal to "Admin". 
* `.lower()` is used to make sure that if admin is lower case, it still wont be deleted.
* `.find_one()` is used because one specific recipe is being targetted.
* I defined the variable `the_recipe =  mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})` to call to the specific recipe that will now be updated.

```

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
```
* In this function once again, a specific recipe is being targetted so the recipe ID is called to. 
* The method her is POST as well because new information pertaining to a specific recipe is being added/changed
* All of the varriables (recipe_name, ingredients, directions, nutrition, recipe_by, recipe_image) are defined as `request.form.get()` to retrieve the data from the form to check if `.isspace() ==True:` if it is, then in the return statement, `return render_template('error_editrecipe.html', recipes=the_recipe, types=mongo.db.types.find())`
* The recipes variable cantains parameters that are values in inputs in the update recipe form. The `:request.form.get()` pulls that info out of the database to fill the form's values.
* The final return statement then, pulls the `url_for('view_recipe', recipe_id=recipe_id)` to show user the recipe that was just updated by the user.

```
@app.route('/delete_recipe/<recipe_id>')
#function located in the modal to delete the recipe
def delete_recipe(recipe_id):
    recipes =  mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    if recipes['recipe_by'].lower() == 'admin':
        return render_template('error_recipedetails.html', types=mongo.db.types.find(), from_scratch=mongo.db.recipes.find({'_id': ObjectId(recipe_id)})) 
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('all_recipes'))
```
* In this function once again, a specific recipe is being targetted so the recipe ID is called to. 
* In the IF statement, we are checking the recipe_by key in the database to see if it is `== 'admin:` This is to prevent recipes created by the admin from being deleted. 
* If the recipe_by key is equal to 'admin', then it renders the template `error_recipedetails.html` to take the user back to the page that will display the error message with an explanation for the error. 
* `.lower()` is used to check for the lower case version of Admin so neither uppercase or lowercase Admin will be deleted either.
* `.remove({'_id': ObjectId(recipe_id)})` is then able to remove any recipe that is not created by admin. 
* `return redirect(url_for('all_recipes'))` then redirects to the all recipes page for the user to browse more recipes. 


### Bugs Discovered
* Solved Bugs:
    * When editing a recipe, the recipe type appears automatically as beef and then does not save the recipe type after editing. To fix this, I needed to edit the name attribute in the function to be 'type'. 
        * Also the value attribute needed to be changed to `value="{{x['type']}}"`
    * Modal not rendering from delete recipe option. Modal was not inside of For-Loop to be connected to database
    * View Recipe details: page was appearing with no recipe as if one was not triggered. used `href="{{url_for('view_recipe', recipe_id=recipes._id)}}"` to trigger specific id for that recipe
    * Same issue above basically to direct user to view recipe just added/updated. needed to adjust the href and the render_template in the function to direct the user to the new or updated recipe based on specific ID of that recipe.
    * User able to submit recipe using " " or null values, still exploring and researching the issue. used the `.isspace()` method to check the fields in the database to look for space characters. will not submit form with only space characters for any field.

### Further Testing

* Asked fellow students, tutors, and mentor to look at my app on a range of devices to report any bugs found.

## Deployment

1. Go to heroku.com dashboard
2. Click "Create New App"
3. Make app name: from-scratch-recipe-app
4. Chose region: United States
5. Click "Create App"
6. Upon app being created, click the "Deploy" tab
7. Scroll down to "Deploy using Heroku Git"
8. Use the following commands as instructed below:
    ``` 
    heroku login
    Enter your Heroku credentials:
    Email: [Enter email hit enter]
    Password: [Enter password]
    Logged in as acallender@live.sscc.edu
    git init
    git add .
    git commit -m "Initial Commit"
    heroku git:remote -a from-scratch-recipe-app
    set git remote heroku to URL for heroku app
    sudo pip3 freeze --local > requirements.txt
    git add .
    git commit -m "Added requirements.txt file"
    git push heroku master
    echo web: python recipe.py > Procfile
    git add .
    git commit -m "Added Procfile"
    git push heroku master
    heroku ps:scale web=1
    scaling dynos.. done, now running web at 1:Free
    ```
9. To explain the above: in the command line you enter your heroku login and it prompts you for your credentials. After your credentials are verified, 
it tells you you're logged in. You then add the heroku login and info into your github repo with the git init, git add, and git commit commands. 
Then, you link the in the heroku master with the git:remote command. this sets the url for heroku app. Create the requirements.txt file and Procfile 
so the app will deploy correctly. After that you push to heroku nmaster.
10. Go back to heroku.com
11. In open view of the app, Click settings
12. Scroll to config variables
13. Set IP to 0.0.0.0 and click add
14. Set PORT to 5000 and click add
15. Open App and the app opens in the browser


## Credits

### Content
* All info about recipes was derived directly from [Allrecipes](https://www.allrecipes.com/recipes/)
* Code was derrived from myself, Studying the Modules in the previous sections, Tutor support, and from exploring various web entities with forums, such as: [W3Schools](https://www.w3schools.com/), [Stack Overflow](https://stackoverflow.com/), and [Slack](https://slack.com/).

### Media
* The photos used in my webpage were from Google Images


### Acknowledgements
* I recieved inspiration for this project from The Code Institute's Guidlines for Milestone Project 3

