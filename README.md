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
I wanted to develop an app that made it easy and simple for those generation to access on any device.

The app is fully functional on all screen sizes with extensive testing for each feature.

* User Stories:
    * As a Family member interested in browsing the recipes, I visit the app and on the home page 4 featured recipes are displayed. 
    If I would like to use the Navbar and select the All Recipes option, I am directed to the page That has all of the recipes listed on it. 
    * If I am a user that is browsing the recipes and I find a recipe I am interested in, if I click on that recipe image, The app directs me to View the Full recipe. That recipe is displayed with all of the appropriate Information to make that recipe. 
    * If I am browsing a recipe and view the full recipe, In the bottom right hand cornner is a button that allows me to hover it to get all the options for that recipe. Within the button I can delete the recipe, add a recipe, or edit the recipe.
        * Delete: The user who would like to delete the recipe can do so by clicking the trashcan option in the View recipe page. From there a modal opens to ask the user if they are sure They would like to delete. After the user selects yes, to delete the user is redirected to the home page.
        * Edit: The user who would like to edit the recipe can do so by clicking the pencil option in the View recipe page. From there, a new page is opened that allows the user to make edits to the Recipe. Each field in the edit recipe form Is prefilled with the deatails of that particular 
        recipe to be edited. When the user has made the edits they would like to make, they will submit the form and be directed to view the recipe that was just edited in the View recipe page as an updated recipe.
        * Add: The user who would like to add a recipe may do so from the home page in the callout, from the button discussed above, or at anytime in the Navbar. If the user selects any of these buttons a modal is triggered that give the user all of the appropriate fields to submit the recipe to the app. 
        After the user submits the completed form the recipe is immediatly displayed in the View recipe page. This allows the user to look at the recipe just added.

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
    * Contains background and a breif description of what the app is and an option to add a recipe (toggles modal)
* List of all recipes
    * Available on home page and on a seperate page for functionality purposes. 
* Modal #1
    * Gives a form for the user to add a recipe
* Modal #2 
    * Asks user if they are sure they would like to delete the recipe.
* Recipe Details View
    * After clicking the recipe image all of the recipe details are displayed on a new page.
* Floating action button on View Recipe Details page.
    * This button pulsates to get user attention, when hovered the option to add, edit, and delete the recipe are shown. ADD toggles modal, EDIT directs to new page, DELETE toggles second modal

### Features left to Implement 
* Log In/Register
    * A feature I would like to implement with more time to gain the skills to use this feature.
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
        * Use the Add Recipe button on homepage callout
        * Each of the above options triggers the add_recipe function, opens modal
            * The Modal that opens contains the form needed to add the recipe and for the user to give all the appropriate information.
            * Each form input is required.
            * Input fields: Recipe Name | Recipe Type(with select scroll bar options) | Ingredients | Directions | Serves how many people? | Nutrition Facts | Recipe by; | and the Recipe Image input 
            * The user then submits the form triggering the insert_recipe function. This function inserts the new recipe into the mongodb database. A message appears that tells the user they can now view the recipe below, after hitting okay, the user is directed to the view recipe page of the newly added recipe.
            
    * Edit a Recipe
        * While viewing the details of any recipe the user can update the recipe
        * hover over pulsating button (bottom right hand corner) to reveal the edit recipe option 
        * After clicking the edit recipe button (triggering the edit_recipe function), the user is directed to the editrecipe.html page:
            * This form is identical to the add recipe form, except the input fields are filled with the information matching the recipe to be updated
            * When the form is submitted it triggers the update_recipe function. This function changes the recipe based on the new user input.  A message appears that tells the user they can now view the updated recipe below, after hitting okay, the user is directed to the view recipe page of the newly updated recipe. 
    * Delete a Recipe
        * While viewing the details of any recipe the user can delete the recipe
        * hover over pulsating button (bottom right hand corner) to reveal the delete recipe option
         * After clicking the delete recipe button it opens the confirm deletion modal:
            * The modal asks if the user is sure they would like to delete the seleted recipe,
            * If the user clicks the delete button the delete_recipe function is triggered and the user is directed back to the home page via the get_recipe function.
            * If the user hits cancel, the modal closes.

### Bugs Discovered
* Solved Bugs:
    * When editing a recipe, the recipe type appears automatically as beef and then does not save the recipe type after editing.
    * Modal not rendering from delete recipe option. Modal was not inside of For-Loop to be connected to database
    * View Recipe details: page was appearing with no recipe as if one was not triggered. used href="{{url_for('view_recipe', recipe_id=recipes._id)}}" to trigger specific id for that recipe
    * Same issue above basically to direct user to view recipe just added/updated. needed to adjust the href and the render_template in the function to direct the user to the new or updated recipe based on specific ID of that recipe.
* Unsolved Bugs
    * User able to submit recipe using " " or null values, still exploring and researching the issue.

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
* Code was derrived from myself, Studying the Modules in the previous sections, Tutor support, and from exploring various web entities

### Media
* The photos used in my webpage were from Google Images


### Acknowledgements
* I recieved inspiration for this project from The Code Institute's Guidlines for Milestone Project 3

