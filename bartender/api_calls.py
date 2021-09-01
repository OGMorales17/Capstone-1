

# @app.route('/')
# def show_drinks_form():
#     cocktails = most_popular_cocktails()
#     return render_template("home.html", cocktails=cocktails)


# @app.route('/random_cocktails')
# def random_drinks_form():
#     cocktails = random_cocktails()
#     return render_template("random_cocktails.html", cocktails=cocktails)


# ##############################################################################
# # API calls


# @app.route('/index')
# def drink_by_name():
#     name = request.args['name']
#     res = requests.get(f"{API_BASE_URL}/{API_SECRET_KEY}/search.php",
#                        params={'s': name})

#     data = res.json()
#     drinks = data['drinks']

#     cocktails = []

#     for drink in drinks:

#         ingredients = []
#         measurements = []

#         for key in drink:
#             if "strIngredient" in key and drink[key] != None:
#                 ingredients.append(drink[key])
#             if "strMeasure" in key and drink[key] != None:
#                 measurements.append(drink[key])

#         cocktail = {
#             'id': drink['idDrink'],
#             'name': drink['strDrink'],
#             'thumb': drink['strDrinkThumb']
#         }

#         cocktails.append(cocktail)

#     return render_template('index.html', cocktails=cocktails, zip=zip)


# @app.route('/drink_details')
# def details_by_id():
#     drink_id = request.args['drink_id']
#     res = requests.get(f"{API_BASE_URL}/{API_SECRET_KEY}/lookup.php",
#                        params={'i': drink_id})

#     data = res.json()
#     drinks = data['drinks']

#     cocktails = []

#     for drink in drinks:

#         ingredients = []
#         measurements = []

#         for key in drink:
#             if "strIngredient" in key and drink[key] != None:
#                 ingredients.append(drink[key])
#             if "strMeasure" in key and drink[key] != None:
#                 measurements.append(drink[key])

#         cocktail = {
#             'id': drink['idDrink'],
#             'name': drink['strDrink'],
#             'thumb': drink['strDrinkThumb'],
#             'instructions': drink['strInstructions'],
#             'ingredients': ingredients,
#             'measurements': measurements
#         }

#         cocktails.append(cocktail)

#     return render_template('drink_details.html', cocktails=cocktails, zip=zip)


# ##############################################################################


# def most_popular_cocktails():
#     res = requests.get(f"{API_BASE_URL}/{API_SECRET_KEY}/popular.php")

#     data = res.json()
#     drinks = data['drinks']

#     cocktails = []

#     for drink in drinks:

#         ingredients = []
#         measurements = []

#         for key in drink:
#             if "strIngredient" in key and drink[key] != None:
#                 ingredients.append(drink[key])
#             if "strMeasure" in key and drink[key] != None:
#                 measurements.append(drink[key])

#         cocktail = {
#             'id': drink['idDrink'],
#             'name': drink['strDrink'],
#             'thumb': drink['strDrinkThumb']
#         }

#         cocktails.append(cocktail)

#     return cocktails


# def random_cocktails():
#     res = requests.get(
#         f"{API_BASE_URL}/{API_SECRET_KEY}/randomselection.php")

#     data = res.json()
#     drinks = data['drinks']

#     random_cocktails = []

#     for drink in drinks:

#         ingredients = []
#         measurements = []

#         for key in drink:
#             if "strIngredient" in key and drink[key] != None:
#                 ingredients.append(drink[key])
#             if "strMeasure" in key and drink[key] != None:
#                 measurements.append(drink[key])

#         cocktail = {
#             'id': drink['idDrink'],
#             'name': drink['strDrink'],
#             'thumb': drink['strDrinkThumb']
#         }

#         random_cocktails.append(cocktail)

#     return random_cocktails


# ##############################################################################


# @app.route('/category')
# def drink_by_category():

#     category = request.args.get('category')

#     cocktails = []
#     if category:
#         res = requests.get(f"{API_BASE_URL}/{API_SECRET_KEY}/filter.php",
#                            params={'c': category})

#         data = res.json()
#         drinks = data['drinks']

#         cocktails = []

#         for drink in drinks:

#             cocktail = {
#                 'id': drink['idDrink'],
#                 'name': drink['strDrink'],
#                 'thumb': drink['strDrinkThumb']
#             }

#             cocktails.append(cocktail)

#     return render_template('category.html', cocktails=cocktails, zip=zip)


# @app.route('/filter_alcohol')
# def drink_by_alcoholic():

#     filter_alcohol = request.args.get('filter_alcohol')

#     cocktails = []
#     if filter_alcohol:
#         res = requests.get(f"{API_BASE_URL}/{API_SECRET_KEY}/filter.php",
#                            params={'a': filter_alcohol})

#         data = res.json()
#         drinks = data['drinks']

#         cocktails = []

#         for drink in drinks:

#             cocktail = {
#                 'id': drink['idDrink'],
#                 'name': drink['strDrink'],
#                 'thumb': drink['strDrinkThumb']
#             }

#             cocktails.append(cocktail)

#     return render_template('filter_alcohol.html', cocktails=cocktails, zip=zip)


# @app.route('/ingredient')
# def search_by_ingredients():

#     ingredient = request.args.get('ingredient')
#     cocktails = []

#     if ingredient:

#         res = requests.get(f"{API_BASE_URL}/{API_SECRET_KEY}/filter.php",
#                            params={'i': ingredient})

#         data = res.json()
#         drinks = data['drinks']

#         cocktails = []

#         for drink in drinks:

#             cocktail = {
#                 'id': drink['idDrink'],
#                 'name': drink['strDrink'],
#                 'thumb': drink['strDrinkThumb']
#             }

#             cocktails.append(cocktail)

#     return render_template('ingredient.html', cocktails=cocktails, zip=zip)
