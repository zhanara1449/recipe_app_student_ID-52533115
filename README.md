# recipe_app_student_ID-52533115
Project assignment in Advanced Programming



# Explanation of Data

This is a dataset about the explorer recipes. We have 2 linked tables. One about ingredients, one about the recipes. 

# Structure 

project/
│
├── setup_db.py
├── app.py
├── database.db
├── templates/
│   ├── base.html
│   ├── cuisine.html
│   ├── detail.html
│   ├── error.html
│   ├── index.html
│   ├── detail.html
│   └── stats.html
│
├── static/
│   └── style.css

# Main Pieces
-main folder -  'recipe_app_student_ID-52533115' - (appologies for long title)
- app's folder 'back-end'
- 'back-end/app.py' This is  main flask app. 
- 'ingredients.csv' This is ingredients record. It has ingredient_id,recipe_id,ingredient_name,quantity,unit
- 'recipes.csv' This is where the recipes.It has recipe_id,name,cuisine,cooking_time,difficulty
- 'back-end/templates/base.html' Base flask  design for all pages
- 'back-end/templates/index.html' Main page
- 'back-end/templates/search.html' Page for searching data, with form user can make deeper searching
- 'back-end/templates/error.html'Error page: two errors available — one when the page did not load (Error 404), and one when the search form is filled with mistakes.
- 'back-end/templates/stats.html' -showing statistics divided by category, country, and quantity of recipes in the application.
- 'back-end/templates/cuisine.html'  page for each category (Example coutry Greek -page [cuisine/](http://127.0.0.1:5000/cuisine/Greek))
- 'back-end/templates/detail.html' page for the current food.It shows recipe by  ingredients, quantity and unit


# How to Run the app

First, clone the repository from GitHub using URL

In terminal after cloning:
- open folder recipe_app_student_ID-52533115 (cd recipe_app_student_ID-52533115)
- open folder back-end (cd back-end)
- python3 -m venv. venv
- source .venv/bin/activate *or .venv/Scripts/activate on Windows*
- python -m pip install
- python.exe -m pip install --upgrade pip (if required)
- pip install flask 
- python manage.py test  
- python -m flask --app app run 


# How to open page 
URL https://recipe-app-student-id-52533115-3.onrender.com 
Git-hub https://github.com/zhanara1449/recipe_app_student_ID-52533115.git  