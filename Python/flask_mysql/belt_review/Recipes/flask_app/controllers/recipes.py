from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        all_recipes = Recipe.get_all()
        logged_user = User.get_by_id({'id' : session['user_id']})
        return render_template('dashboard.html', user = logged_user, recipes = all_recipes)
    return redirect('/')

@app.route('/recipes/new')
def new():
    if 'user_id' in session:
        return render_template('new_recipe.html')
    return redirect('/')

@app.route('/recipes/create', methods = ['POST'])
def create():
    if 'user_id' in session:
        if Recipe.validate(request.form):
            data = {
                **request.form, 'user_id' : session['user_id']
            }
            Recipe.create(data)
            return redirect('/dashboard')
        return redirect('/recipes/new')
    return redirect('/')

@app.route('/recipes/<int:recipe_id>/edit')
def edit(recipe_id):
    if 'user_id' in session :
        recipe = Recipe.get_one_by_id({'id' : recipe_id})
        if recipe.user_id == session['user_id']:
            return render_template('edit_recipe.html', recipe = recipe)
        return render_template('danger.html', recipe=recipe)
    return redirect('/')

@app.route('/recipes/<int:recipe_id>/update', methods = ['POST'])
def update(recipe_id):
    if 'user_id' in session :
        if Recipe.validate(request.form):
            data = {
                **request.form, 'id' : recipe_id
            }
            Recipe.update(data)
            return redirect('/dashboard')
        recipe = Recipe.get_one_by_id({'id' : recipe_id})
        return render_template('edit_recipe.html', recipe = recipe)
    return redirect('/')

@app.route('/recipes/<int:recipe_id>')
def view(recipe_id):
    if 'user_id' in session :
        logged_user = User.get_by_id({'id' : session['user_id']})
        recipe = Recipe.get_one_by_id({'id' : recipe_id})
        return render_template('view_recipe.html', user=logged_user, recipe=recipe)
    return redirect('/')

@app.route('/my_recipes')
def my_recipes():
    if 'user_id' in session :
        logged_user = User.get_by_id({'id' : session['user_id']})
        recipes = Recipe.get_by_user({'user_id' : session['user_id']})
        return render_template('my_recipes.html', recipes=recipes, user=logged_user)
    return redirect('/')
