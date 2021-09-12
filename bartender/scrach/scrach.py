# Inside the ingredients file

#     <p>
#     <button class = "btn btn-primary" type = "button" data-bs-toggle = "collapse" data-bs-target = "#collapseExample" aria-expanded = "false" aria-controls = "collapseExample" >
#     Ingredients
#     </button >
#     <div class = "collapse" id = "collapseExample" >
#     </p>

#      <div class = "card card-body" >
#         <!-- {% for ing in ingredients % }
#         <ul > {{ing['strIngredient1']}} < /ul >
#         { % endfor % }       - ->
#         <!-- Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger. - ->
#       </div>
#     </div>
# -------------------------------------------------------------------------------------------->


# Create an autocomplete for the ingredients
# Give the users a list of all ingredients that can ve add to a drink
# @app.route('/ingredient')
# def list_of_ingredients():
#     ingredients = all_ingredients()

#     return render_template("drinks/ingredient.html", ingredients=ingredients)

# -------------------------------------------------------------------------------------------->

# def all_ingredients():
#     res = requests.get(f"{API_BASE_URL}/{API_SECRET_KEY}/list.php?i=list")

#     data = res.json()
#     drinks = data['drinks']
#     all_cocktails = []

#     for drink in drinks:
#         all_cocktails.append(drink)

#     return all_cocktails


# -------------------------------------------------------------------------------------------->

# @app.route('/users/favorite/<int:drink_id>', methods=["POST"])
# def add_favorite(drink_id):
#     """Add Drink id to user favorite."""

#     user_id = request.form.get('user_id')
#     # user = User.query.get_or_404(user_id)

#     # check if drink with drink_id exists
#     # get drink details

#     # check if drink with id exists

#     drink_object = Drink.query.filter_by(drink_info=str(drink_id)).first()

#     if not drink_object:
#         res = requests.get(f"{API_BASE_URL}/{API_SECRET_KEY}/lookup.php",
#                            params={'i': drink_id})

#         data = res.json()
#         drinks = data['drinks'][0]
#         drink_id = drinks['idDrink']
#         drink_name = drinks['strDrink']

#         new_drink = Drink(drink_name=drink_name, drink_info=drink_id)
#         db.session.add(new_drink)
#         db.session.commit()

#     else:

#         drink_id_in_table = drink_object.id

#     try:
#         new_fav = Favorite(user_id=user_id, drink_id=drink_id_in_table)
#         db.session.add(new_fav)
#         db.session.commit()

#         return {'success': True}

#     except:
#         return {'success': False}


# ------------------------------ models.py ---------------------------------

# class User(db.Model):
#     """User in the system."""

#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True,)

#     email = db.Column(db.Text, nullable=False, unique=True,)
#     username = db.Column(db.Text, nullable=False, unique=True,)
#     password = db.Column(db.Text, nullable=False,)

#     def __repr__(self):
#         return f"<User #{self.id}: {self.username}, {self.email}>"

#     @classmethod
#     def signup(cls, username, password, email):
#         """Sign up user.

#         Hashes password and adds user to system.
#         """

#         hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

#         user = User(
#             username=username,
#             email=email,
#             password=hashed_pwd,
#         )

#         db.session.add(user)
#         return user

#     @classmethod
#     def authenticate(cls, username, password):
#         """Find user with `username` and `password`.

#         This is a class method (call it on the class, not an individual user.)
#         It searches for a user whose password hash matches this password
#         and, if it finds such a user, returns that user object.

#         If can't find matching user (or if password is wrong), returns False.
#         """

#         user = cls.query.filter_by(username=username).first()
#         if user:
#             is_auth = bcrypt.check_password_hash(user.password, password)
#             if is_auth:
#                 return user
#         return False


# class Drink(db.Model):
#     """  """
#     __tablename__ = 'drinks'

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     drink_id = db.Column(db.Text, nullable=False, unique=True)
#     drink_name = db.Column(db.Text, nullable=False, unique=True)
#     drink_thum = db.Column(db.Text, nullable=False, unique=True)
#     # user_id = db.Column(db.Integer, db.ForeignKey(
#     #     'users.id', ondelete='cascade'))


# class Favorite(db.Model):
#     """  """

#     __tablename__ = 'favorites'

#     id = db.Column(db.Integer, primary_key=True)

#     user_id = db.Column(db.Integer, db.ForeignKey(
#         'users.id', ondelete='cascade'))
#     drink_id = db.Column(db.Integer, db.ForeignKey(
#         'drinks.id', ondelete='cascade'))


# class Feedback(db.Model):
#     """User giving feedback to the drinks."""

#     __tablename__ = 'feedbacks'

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)

#     user_id = db.Column(db.Integer, db.ForeignKey(
#         'users.id', ondelete='cascade'))
#     drink_id = db.Column(db.Integer, db.ForeignKey(
#         'drinks.id', ondelete='cascade'))
#     rating = db.Column(db.Integer, nullable=False)


# ------------------------------------------------------------------------------------

# class UserDrink(db.Model):
#     __tablename__ = 'user_drinks'

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     drink_id = db.Column(db.Text, db.ForeignKey(
#         'drink.id', ondelete='cascade'), nullable=False,)
#     user_id = db.Column(db.Integer, db.ForeignKey(
#         'users.id', ondelete='cascade'), nullable=False,)


# class Drink(db.Model):
#     """  """
#     __tablename__ = 'drinks'

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     drink_id = db.Column(db.Text, nullable=False, unique=False)
#     drink_name = db.Column(db.Text, nullable=False, unique=False)
#     drink_thum = db.Column(db.Text, nullable=False, unique=False)
#     # user_id = db.Column(db.Integer, db.ForeignKey(
#     #     'users.id', ondelete='cascade'), nullable=False,)

# ------------------------------------------------------------------------------------


# @app.route('/users/<int:user_id>')
# def users_show(user_id):
#     """Show user profile."""
# user = User.query.get_or_404(user_id)

# print('Current User', user)

# cocktail = FavoriteDrink.query.order_by(FavoriteDrink.user_id).all()

# for drink in cocktail:
#     print(
#         f'{drink.drink_id} - {drink.drink_name} - {drink.drink_thum} - {drink.user_id}')

# return render_template('users/favorite.html', user=user)


class Feedback(db.Model):
    """User giving feedback to the drinks."""

    __tablename__ = 'feedbacks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id', ondelete='cascade'))
    drink_id = db.Column(db.Integer, db.ForeignKey(
        'favorite_drinks.id', ondelete='cascade'))
    rating = db.Column(db.Integer, nullable=False)
