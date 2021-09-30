# Everybodybarman - Drinks App


#### <div align='center'>Try the App Here</div>  
#### <div align='center'>https://everybodybarman.herokuapp.com/</div>  


<br>

 This web app presents a wide variety of drinks to users. Each drink includes its name, picture and recipe. The twenty cocktail presented at the landing are with in the most populars in the data base, a search by name is also an option. The recipe will be presented by cliking on details. To save any drink the user must sign up.
 

 The user will be able to narrow down the search in the navbar by clicking in Category, Alcohol/Non Alcohol or Ingredients.

 

 On the very bottom of the page a footer has placed, where a link to a random selection of teen cocktail will present everytime is click, a search by name is also an option in the same. The other option is clicking on select by the first letter, which will render a new temple where the user will be able to type in any of the letter or number above the imput bar.
  
 This project consumes data from <a>[TheCocktailDB API](https://www.thecocktaildb.com/)</a> patreon supporter version, the documentation can be found  <a>[here](https://www.thecocktaildb.com/api.php)</a>. 
<br> 


## Technologies used



 <a href="https://www.w3.org/TR/html5/" title="HTML5"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" alt="HTML5" width="21px" height="21px"></a> &nbsp;<a href="https://www.w3.org/TR/CSS/" title="CSS3"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" alt="CSS3" width="21px" height="21px"></a> &nbsp;<a href="https://getbootstrap.com/" title="Bootstrap"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg" alt="Bootstrap" width="21px" height="21px"></a> &nbsp; <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" title="JavaScript"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="JavaScript" width="21px" height="21px"></a> &nbsp;<a href="https://www.python.org/" title="Python"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" width="21px" height="21px"></a> &nbsp;<a href="https://git-scm.com/" title="Git"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" alt="Git" width="21px" height="21px"></a> &nbsp;<a href="https://code.visualstudio.com/" title="Visual Studio Code"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" alt="Visual Studio Code" width="21px" height="21px"></a> &nbsp; <a href="https://jinja.palletsprojects.com/en/3.0.x/" title="JINJA"><img src="readme_files/jinja2.png" alt="JINJA" width="21px" height="21px" style="background-color: white"></a> &nbsp; <a href="https://www.heroku.com/" title="Heroku"><img src="readme_files/heroku.jpeg" alt="Heroku" width="21px" height="21px"></a> &nbsp; <a href="https://www.postgresql.org/" title="Postgres"><img src="readme_files/postgres.png" alt="Postgres" width="21px" height="21px"></a> &nbsp; <a href="https://fontawesome.com/" title="FontAwesome"><img src="readme_files/fontawesome.png" alt="FontAwesome" width="21px" height="21px"></a> &nbsp; <a href="https://flask.palletsprojects.com/en/1.1.x/" title="Flask"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" alt="Flask" width="40px" height="21px" style="background-color: white"></a> &nbsp; <a href="https://www.sqlalchemy.org/" title="Git"><img src="readme_files/sql_alchemy_logo.jpeg" alt="WTForms" width="70px" height="21px"></a> &nbsp; <a href="https://wtforms.readthedocs.io/en/2.3.x/#" title="WTForms"><img src="readme_files/wtforms.png" alt="SQLAlchemy" width="80px" height="21px"></a>&nbsp;<a href="https://devicon.dev/" title="Devicon"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/devicon/devicon-original.svg" alt="Devicon" width="80px" height="21px"></a>


## Installation 

### Before You Begin
You will need python3 and pip3 installed for this project. You will also need to setup a Postgres Database if you want to allow the user to save each drink, remember that in order to save the drink the user must login or signup, for that you will need a DB.
<br>
<hr>

#### Installation Instructions

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
