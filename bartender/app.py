import os
from re import search

from flask import Flask, render_template, request, flash, redirect, session, g, abort
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError
import requests
import psycopg2

from forms import UserAddForm, UserEditForm, LoginForm, FeedbackForm
from models import db, connect_db, User, Feedback, Favorite, Drink
from secret import API_SECRET_KEY, API_BASE_URL


CURR_USER_KEY = "curr_user"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql:///bartender')
app.config['SECRET_KEY'] = (os.environ.get('API_SECRET_KEY', 'Is a secret'))


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# toolbar = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def show_drinks_form():

    return render_template("home.html")


@app.route('/index')
def drink_by_name():
    name = request.args['name']
    res = requests.get(f"{API_BASE_URL}/{API_SECRET_KEY}/search.php",
                       params={'s': name})

    data = res.json()

    cocktail_name = data['drinks'][0]['strDrink']
    cocktail_thumb = data['drinks'][0]['strDrinkThumb']
    cocktail_instructions = data['drinks'][0]['strInstructions']

    ingredients = []
    measurements = []

    i = 1

    while i <= 15:

        cocktail_ingredient = data['drinks'][0]['strIngredient' + str(i)]
        cocktail_measure = data['drinks'][0]['strMeasure' + str(i)]

        if cocktail_ingredient != None:
            ingredients.append(cocktail_ingredient)

        if cocktail_measure != None:
            measurements.append(cocktail_measure)

        i += 1

    cocktail_instructions = data['drinks'][0]['strInstructions']
    cocktail_category = data['drinks'][0]['strCategory']

    cocktail = {'name': cocktail_name, 'thumb': cocktail_thumb, 'ingredients': ingredients,
                'measurements': measurements, 'instructions': cocktail_instructions, 'category': cocktail_category}

    return render_template('index.html', cocktail=cocktail)


##############################################################################
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


@app.route('/logout')
def logout():
    """Handle logout of user."""

    do_logout()

    flash("You have successfully logged out.", 'success')
    return redirect("/login")


##############################################################################
# Homepage and error pages


# @app.route('/')
# def homepage():
#     """Show homepage:

#     - anon users: no messages
#     - logged in: 100 most recent messages of followed_users
#     """

#     if g.user:
#         following_ids = [f.id for f in g.user.following] + [g.user.id]

#         messages = (Message
#                     .query
#                     .filter(Message.user_id.in_(following_ids))
#                     .order_by(Message.timestamp.desc())
#                     .limit(100)
#                     .all())

#         liked_msg_ids = [msg.id for msg in g.user.likes]

#         return render_template('home.html', messages=messages, likes=liked_msg_ids)

#     else:
#         return render_template('home-anon.html')


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

@app.after_request
def add_header(req):
    """Add non-caching headers on every request."""

    req.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    req.headers["Pragma"] = "no-cache"
    req.headers["Expires"] = "0"
    req.headers['Cache-Control'] = 'public, max-age=0'
    return req
