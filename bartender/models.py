from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()

# In the Drink table add, drink_id, thum, and remove drink_info
# add a function in the User table that will check if drink_id is within User Favorite, if found return it.
# In the user favorite.html only show the cocktail name and thum, but if the user click on detail, then make an API request of just for that expecific drink_id, and render into drink detail page

# In the Favorite table remove the FK to the Drink id and make a new one to the drink_id

# In the Feedback table remove the FK to the Drink id and make a new one to the drink_id, also remove content from the table and use the rating only, this way I'm not letting the user write conten that may not be appropiate to the view of others.


class User(db.Model):
    """User in the system."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True,)

    email = db.Column(db.Text, nullable=False, unique=True,)
    username = db.Column(db.Text, nullable=False, unique=True,)
    password = db.Column(db.Text, nullable=False,)
    favorite_drinks = db.relationship('FavoriteDrink')

    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}>"

    @classmethod
    def signup(cls, username, password, email):
        """Sign up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            username=username,
            email=email,
            password=hashed_pwd,
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.

        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.

        If can't find matching user (or if password is wrong), returns False.
        """

        user = cls.query.filter_by(username=username).first()
        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user
        return False


class FavoriteDrink(db.Model):
    """  """
    __tablename__ = 'favorite_drinks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    drink_id = db.Column(db.Text, nullable=False, unique=False)
    drink_name = db.Column(db.Text, nullable=False, unique=False)
    drink_thum = db.Column(db.Text, nullable=False, unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id', ondelete='cascade'), nullable=False,)


class Feedback(db.Model):
    """User giving feedback to the drinks."""

    __tablename__ = 'feedbacks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id', ondelete='cascade'))
    drink_id = db.Column(db.Integer, db.ForeignKey(
        'favorite_drinks.id', ondelete='cascade'))
    rating = db.Column(db.Integer, nullable=False)


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)
