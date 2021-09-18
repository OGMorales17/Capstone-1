import os
from re import M, search

from flask import Flask, render_template, request, flash, redirect, session, g, abort, url_for
from sqlalchemy.exc import IntegrityError
import requests
import psycopg2
import itertools

from forms import UserAddForm, LoginForm, PasswordResetForm
from models import db, connect_db, User, FavoriteDrink
from secret import API_SECRET_KEY, API_BASE_URL
from helpers import get_cocktails_from_api_response


CURR_USER_KEY = "curr_user"

app = Flask(__name__)
app.jinja_env.filters['zip'] = zip

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL').replace("://", "ql://", 1) or 'postgresql:///bartender'
app.config['SECRET_KEY'] = (os.environ.get('API_SECRET_KEY', 'Is a secret'))


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)


# User signup/login/logout


@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup.

    Create new user and add to DB. Redirect to home page.

    If form not valid, present form.

    If the there already is a user with that username: flash message
    and re-present form.
    """
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]
    form = UserAddForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data,
                password=form.password.data,
                email=form.email.data,
            )
            db.session.commit()

        except IntegrityError as e:
            flash("Username already taken", 'danger')
            return render_template('users/signup.html', form=form)

        do_login(user)

        return redirect("/")

    else:
        return render_template('users/signup.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data,
                                 form.password.data)

        if user:
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect("/")

        flash("Invalid credentials.", 'danger')

    return render_template('users/login.html', form=form)


#######################################################
# This next two function home_anon and under_age need more work

# @app.route('/')
# def home_anon():

#     return render_template("home_anon.html")


# @app.route('/under_age')
# def under_age():

#     return render_template("/drinks/under_age.html")


@app.route('/')
def show_drinks_form():
    cocktails = most_popular_cocktails()

    return render_template("home.html", cocktails=cocktails)


@app.route('/random_cocktails')
def random_drinks_form():
    cocktails = random_cocktails()

    return render_template("drinks/random_cocktails.html", cocktails=cocktails)


@app.route('/letter')
def letter_drinks_form():

    return render_template("drinks/letter.html")


@app.route('/index')
def drink_by_name():
    name = request.args['name']
    res = requests.get(f"{API_BASE_URL}/{API_SECRET_KEY}/search.php",
                       params={'s': name})

    data = res.json()

    if data.get('drinks') == None:
        flash("No drink name found", "danger")
        return redirect('/')
    else:

        cocktails = get_cocktails_from_api_response(data)

    return render_template('drinks/index.html', cocktails=cocktails)


##############################################################################


@app.route('/random_cocktails')
def by_name_on_random():
    name = request.args['name']
    res = requests.get(f"{API_BASE_URL}/{API_SECRET_KEY}/search.php",
                       params={'s': name})

    data = res.json()
    cocktails = get_cocktails_from_api_response(data)

    return render_template('drinks/index.html', cocktails=cocktails)


@app.route('/search_by_letter')
def search_by_letter():
    letter = request.args['letter']
    res = requests.get(f"{API_BASE_URL}/{API_SECRET_KEY}/search.php",
                       params={'f': letter})

    data = res.json()
    if data.get('drinks') == None:
        flash("No drink name found", "danger")
        return redirect('/letter')
    else:

        cocktails = get_cocktails_from_api_response(data)

    return render_template('drinks/letter.html', cocktails=cocktails)


##############################################################################
# This random_cocktails is going to load a selection of random cocktails by clicking the link in the footer of the page

def random_cocktails():
    res = requests.get(
        f"{API_BASE_URL}/{API_SECRET_KEY}/randomselection.php")

    data = res.json()
    return get_cocktails_from_api_response(data)


##############################################################################
# The navbar route Links

# This most_popular_cocktails function loads the most populars by clicking at the cocktail icon in the navbar
def most_popular_cocktails():
    res = requests.get(f"{API_BASE_URL}/{API_SECRET_KEY}/popular.php")

    data = res.json()
    return get_cocktails_from_api_response(data)


@app.route('/category')
def drink_by_category():

    category = request.args.get('category')
    cocktails = []

    if category:
        res = requests.get(f"{API_BASE_URL}/{API_SECRET_KEY}/filter.php",
                           params={'c': category})

        data = res.json()
        cocktails = get_cocktails_from_api_response(data)

    return render_template('drinks/category.html', cocktails=cocktails)


@app.route('/filter_alcohol')
def drink_by_alcoholic():

    filter_alcohol = request.args.get('filter_alcohol')
    cocktails = []

    if filter_alcohol:
        res = requests.get(f"{API_BASE_URL}/{API_SECRET_KEY}/filter.php",
                           params={'a': filter_alcohol})

        data = res.json()
        cocktails = get_cocktails_from_api_response(data)

    return render_template('drinks/filter_alcohol.html', cocktails=cocktails)


@app.route('/ingredient')
def search_by_ingredients():

    ingredient = request.args.get('ingredient')

    if ingredient:
        res = requests.get(f"{API_BASE_URL}/{API_SECRET_KEY}/filter.php",
                           params={'i': ingredient})

        data = res.json()
        if data.get('drinks') == 'None Found':
            flash("No drink found", "danger")
            return render_template('drinks/ingredient.html')

        else:
            cocktails = get_cocktails_from_api_response(data)
            return render_template('drinks/ingredient.html', cocktails=cocktails)

    return render_template('drinks/ingredient.html')


#############################################################################
# Get all the details of the drink


@app.route('/drink_details')
def details_by_id():
    drink_id = request.args['drink_id']
    res = requests.get(f"{API_BASE_URL}/{API_SECRET_KEY}/lookup.php",
                       params={'i': drink_id})

    data = res.json()
    drinks = data['drinks']

    cocktails = []

    for drink in drinks:

        ingredients = []
        measurements = []

        for key in drink:
            if "strIngredient" in key and drink[key] != None:
                ingredients.append(drink[key])
            if "strMeasure" in key and drink[key] != None:
                measurements.append(drink[key])

        cocktail = {
            'id': drink['idDrink'],
            'name': drink['strDrink'],
            'thumb': drink['strDrinkThumb'],
            'instructions': drink['strInstructions'],
            'ingredients': ingredients,
            'measurements': measurements
        }

        cocktails.append(cocktail)

    return render_template('drinks/drink_details.html', cocktails=cocktails, zip=zip)

##############################################################################
# This reset function is not working at the moment.


@app.route('/reset_account', methods=["GET", "POST"])
def reset_account():
    """Handle user account reset."""

    form = PasswordResetForm()
    # Currently this form is not validating
    if form.validate_on_submit():
        user = User.authenticate(form.username.data,
                                 form.email.data)

        if user:
            # Add logic, change do_login for do_reset, create a do_reset function, that will render a form
            # and this form will delete the current password associate with the user by having the user typing in to the form the
            # newlly created password and redirect to do_login
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect("/")

        flash("Invalid credentials.", 'danger')

    return render_template('users/reset_account.html', form=form)

# -------------------------------------------------------------------------------------------------------


@app.route('/logout')
def logout():
    """Handle logout of user."""

    do_logout()

    flash("You have successfully logged out.", 'success')
    return redirect("/")


##############################################################################
# User Homepage


@app.route('/users/favorite')
def user_favorite():

    user_id = g.user.id
    user = User.query.get_or_404(user_id)

    if user:

        all_drinks = FavoriteDrink.query.filter_by(
            user_id=user_id).order_by(FavoriteDrink.id.desc()).all()

        cocktails = []
        for drink in all_drinks:
            cocktail = {'name': drink.drink_name,
                        'id': drink.drink_id, 'thumb': drink.drink_thum}

            cocktails.append(cocktail)

        return render_template("users/favorite.html", user=user, cocktails=cocktails, show_delete=True)
    else:
        return render_template("users/favorite.html")


@app.route('/users/favorite/<int:drink_id>', methods=["GET", "POST"])
def add_favorite(drink_id):
    """Add Drink id to user favorite."""

    user_id = g.user.id
    user = User.query.get_or_404(user_id)

    drink_object = FavoriteDrink.query.filter_by(
        drink_id=str(drink_id),
        user_id=str(user_id)
    ).all()

    if not drink_object:
        res = requests.get(f"{API_BASE_URL}/{API_SECRET_KEY}/lookup.php",
                           params={'i': drink_id})

        data = res.json()
        drinks = data['drinks'][0]
        drink_id = drinks['idDrink']
        drink_name = drinks['strDrink']
        drink_thum = drinks['strDrinkThumb']

        new_drink = FavoriteDrink(drink_id=drink_id,
                                  drink_name=drink_name, drink_thum=drink_thum, user_id=user_id)

        db.session.add(new_drink)
        db.session.commit()

        return redirect(url_for('user_favorite'))

    else:
        flash("Drink already in favorites!", "danger")
        return redirect(url_for('show_drinks_form'))

# -------------------- Remove the favorite drinks  --------------------------->


@app.route('/users/delete/<int:drink_id>', methods=["GET", "POST"])
def delete_drink(drink_id):
    """Have currently-logged-in-user delete drink."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    user_favorite_drink = FavoriteDrink.query.filter_by(
        drink_id=str(drink_id),
        user_id=str(g.user.id)
    ).first()

    db.session.delete(user_favorite_drink)
    db.session.commit()

    return redirect(f"/users/favorite")


##############################################################################


@app.errorhandler(404)
def page_not_found(e):
    """404 NOT FOUND page."""

    return render_template('404/404.html'), 404


##############################################################################
# Turn off all caching in Flask
#   (useful for dev; in production, this kind of stuff is typically
#   handled elsewhere)
#
# https://stackoverflow.com/questions/34066804/disabling-caching-in-flask

@ app.after_request
def add_header(req):
    """Add non-caching headers on every request."""

    req.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    req.headers["Pragma"] = "no-cache"
    req.headers["Expires"] = "0"
    req.headers['Cache-Control'] = 'public, max-age=0'
    return req
