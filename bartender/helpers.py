def get_cocktails_from_api_response(data):
    drinks = data['drinks']

    cocktails = []

    for drink in drinks:

        cocktail = {
            'id': drink['idDrink'],
            'name': drink['strDrink'],
            'thumb': drink['strDrinkThumb']
        }

        cocktails.append(cocktail)
    return cocktails
# --------------------------------------------------------------------------------------- #
