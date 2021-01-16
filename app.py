# app.py
# from os.path import join, dirname
# from dotenv import load_dotenv
import os
import flask

USERS_UPDATED_CHANNEL = 'users updated'

app = flask.Flask(__name__)


# dotenv_path = join(dirname(__file__), 'sql.env')
# load_dotenv(dotenv_path)

# database_uri = os.environ['DATABASE_URL']


@app.route('/')
def index():
    return flask.render_template("index.html")

if __name__ == '__main__': 
    app.run(
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )