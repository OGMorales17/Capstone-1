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
