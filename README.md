# Bartender 
<br>  

#### <div align='center'>[Try the App Here](https://everybodybarman.herokuapp.com/)</div>  
<br>  

### This web app presents a wide variety of drinks to users. Each drink includes its name, picture and recipe. The recipe will be presented by cliking on details. To save any drink the user must sign up.
<br>  

### There is wide variety of drinks from alcoholic to non-alcoholic. The user will be able to narrow down the search. 
<br>  

### The API that is being used in this app is <a>[TheCocktailDB API](https://www.thecocktaildb.com/)</a> and the documentation can be found  <a>[here](https://www.thecocktaildb.com/api.php)</a>. 
<br> 


## Installation 
<hr>

### Before You Begin
You will need python3 and pip3 installed for this project. You will also need to setup a Postgres Database if you want to allow the user to save each drink, remember that in order to save the drink the user must login or signup, for that you will need a DB.
<br>
<hr>
<br>

#### Installation Instructions

<!-- 1. Get a free API key from ProPublica
    ```sh
    https://www.propublica.org/datastore/api/propublica-congress-api
    ``` -->

1. Clone the repo.
    ```sh
    https://github.com/OGMorales17/Capstone-1.git
    ```

2. Create a virtual environment in the project directory.
    ```sh 
    $ python3 -m venv venv
    ```

3. Start the virtual environment.
    ```sh
    $ source venv/bin/activate
    ```

4. Install required packages.
    ```sh
    $ pip3 install -r requirements.txt
    ```

5. Open the secrets.py file and change the current API_SECRET_KEY and API_BASE_URL for the ones in the fields specified below. 

   
    ```sh
    API_SECRET_KEY = "1"
    API_BASE_URL = "https://www.thecocktaildb.com/api/json/v1/"
    ```
<br>  


_**You will need to set up PostgreSQL database for this application. Once that is done you can move to the next step.**_

<br>  

1. In the terminal.
    ```sh
    $ createdb bartender
    $ ipython
    ```

2. In Ipython.
    ```sh
    In [1]: run app.py
    In [2]: db.create_all()
    In [1]: quit()

    ```

3. Run the app.
    ```sh 
    $ flask run
    ```

4.  Open web browser and run the app on the port for your server.
