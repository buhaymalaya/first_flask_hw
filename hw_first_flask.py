from flask import Flask, request

app = Flask(__name__)

# do not run this with play button on top right
# use flask run instead

# simulate database below
# create and manipulate dicts like json()
# CRUD 
# as soon as server stops, it will reset


# simulate users below

directors = {
    1:{
        'id': 1,
        'username': 'jordan_peele',
        'email': 'jp@gm.com',
        'imdb_rating' : '9/10'
    },
    2:{
        'id': 2,
        'username': 'coen_brothers',
        'email': 'cb@gm.com',
        'imdb_rating': '9/10'
    }
}

# simulate something created linked to directors

movies = {
    1 :{
        'director': 2,
        'title': 'Burn After Reading',
        'description': "A mysterious comedy about two friends with different motives and similar IQ levels",
        'year': '2008'
    },
    2 :{
        'director': 1,
        'title': 'Nope',
        'description': "Horse-wrangling siblings attempting to capture evidence of an unidentified flying object in Agua Dulce, California",
        'year': '2022'
    }
}


# dynamic routing @app.route('/user/<username>') where <think:f'string'>
# convert <'string'> to <int:id> for numeric ids, or <path:subpath>

# HTTP request methods: GET (Read: retrieves data), POST (Create: submits info), PUT (Update: replaces), DEL
# Remember HTTP status codes 100,200, etc


# create routes below
# reference Quickstart flask palletsprojects

@app.route('/') # home page
def home():
    return{
        "This is the Home Page": "Get comfy."
    }


# access users from simulated database above

@app.route('/directors')
def get_directors():
    return {
        'directors' : list(directors.values())
    }


# dynamically retrieve a director's id below:
@app.route('/director/<int:id>', methods=["GET"]) # string contained in <> is also the parameter in function below
def get_ind_director(id):
    if id in directors: # check if director exists
        return {
            'director' : directors[id]
        }
    return {
        'ERROR' : 'INVALID DIRECTOR_ID'
    }

# specify what request method the route can use below (can create another route with same name
# but with a different method later on)
# has to be retrieved through json; cannot be done via browser
# think: Postman ext in VS code and Insomnia on the web

# POST method, create director - Postman

@app.route('/director', methods=["POST"])  
def create_director():
    #ANALYZE REQUEST below
    data = request.get_json() 
    # REQUEST PACKAGE from FLASK: must include at the top import Flask, request; then, get json()
    print(data)
    directors[data['id']] = data
    return {
        'DIRECTOR CREATED SUCCESSFULLY': directors[data['id']]
    }

# open Postman ext, create POST method using local address
# body, raw, json() to communicate with APIs
# input request data in body (see info added for "id":3)
# must us double quotes
# check if input is added through GET /users and local host/users


# PUT Method below: UPDATE Route - Postman

@app.route('/director', methods=["PUT"]) 
def update_director():
    #ANALYZE REQUEST below
    data = request.get_json() 
    if data['id'] in directors:
        directors[data['id']] = data
        return {
            'USER updated': directors[data['id']]
        }
    return {
        'error': 'no user found with that id'
    }

# DELETE method - Postman

@app.route('/director', methods=["DELETE"]) 
def delete_director():
    #ANALYZE REQUEST below
    data = request.get_json() 
    if data['id'] in directors:
        del directors[data['id']]
        return {
            'DIRECTOR deleted': f"{data['username']} erased."
        }
    return {
        'error': 'no user found with that id'
    }
