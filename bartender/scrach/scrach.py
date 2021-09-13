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


# ------------------------------ models.py ---------------------------------

# class Feedback(db.Model):
#     """User giving feedback to the drinks."""

#     __tablename__ = 'feedbacks'

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)

#     user_id = db.Column(db.Integer, db.ForeignKey(
#         'users.id', ondelete='cascade'))
#     drink_id = db.Column(db.Integer, db.ForeignKey(
#         'favorite_drinks.id', ondelete='cascade'))
#     rating = db.Column(db.Integer, nullable=False)
