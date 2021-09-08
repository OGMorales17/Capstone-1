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
