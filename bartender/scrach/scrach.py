# data = res.json()

# cocktails = []
# # iterate over data.drinks
# ingredients = []
# # loop over ingredients
# measurements = []
# # loop over measurements

# i = 1

# while i <= 15:
#     # set current cocktail
#     curcocktail = data['drinks'][i]

#     # create a new cocktail
#     cocktail = {
#         'name': curcocktail['strDrink'],
#         'thumb': curcocktail['strDrinkThumb'],
#         'ingredients': ingredients,
#         'measurements': measurements,
#         'instructions': curcocktail['strInstructions']
#     }
#     # append our cocktail to array
#     cocktails.append(cocktail)

#     i += 1

# return render_template('index.html', cocktails=cocktails)

# ------------------------------------------------------------------------------------>
# @app.route('/index')
# def drink_by_name():
# Searching by name
# name = request.args['name']
# res = requests.get(f"{API_BASE_URL}/{API_SECRET_KEY}/search.php",
#                    params={'s': name})

# data = res.json()

# cocktail_name = data['drinks'][0]['strDrink']
# cocktail_thumb = data['drinks'][0]['strDrinkThumb']
# cocktail_instructions = data['drinks'][0]['strInstructions']

# ingredients = []
# measurements = []

# i = 1

# while i <= 15:

#     cocktail_ingredient = data['drinks'][0]['strIngredient' + str(i)]
#     cocktail_measure = data['drinks'][0]['strMeasure' + str(i)]

#     if cocktail_ingredient != None:
#         ingredients.append(cocktail_ingredient)

#     if cocktail_measure != None:
#         measurements.append(cocktail_measure)

#     i += 1

# cocktail_instructions = data['drinks'][0]['strInstructions']
# cocktail_category = data['drinks'][0]['strCategory']

# cocktail = {'name': cocktail_name, 'thumb': cocktail_thumb, 'ingredients': ingredients,
#             'measurements': measurements, 'instructions': cocktail_instructions, 'category': cocktail_category}

# return render_template('index.html', cocktail=cocktail)


# ---------------------------------------------------------------------------->

# @app.route('/index')
# def drink_by_name():
#     # Searching by the first letter
#     name = request.args['name']
#     res = requests.get(f"{API_BASE_URL}/{API_SECRET_KEY}/search.php",
#                        params={'f': name})

#     data = res.json()

#     cocktails = []
#     # ingredients = []
#     # measurements = []

#     i = 1

#     while i <= 15:

#         curcocktail = data['drinks'][i]
#         # cocktail_ingredient = data['drinks'][0]['strIngredient' + str(i)]
#         # cocktail_measure = data['drinks'][0]['strMeasure' + str(i)]

#         cocktail = {
#             'name': curcocktail['strDrink'],
#             'thumb': curcocktail['strDrinkThumb'],
#             # 'ingredients': ingredients,
#             # 'measurements': measurements,
#             'instructions': curcocktail['strInstructions']
#         }

#         cocktails.append(cocktail)

#         # if cocktail_ingredient != None:
#         #     ingredients.append(cocktail_ingredient)

#         # if cocktail_measure != None:
#         #     measurements.append(cocktail_measure)

#         i += 1

#         print("***************", cocktail['name'])

#     return render_template('index.html', cocktails=cocktails)
